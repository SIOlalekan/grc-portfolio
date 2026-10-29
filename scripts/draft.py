import os, re, yaml, datetime, pathlib
from anthropic import Anthropic

q = yaml.safe_load(open("queue.yml"))
item = next((i for i in q["topics"] if i["status"] == "todo"), None)
if not item:
    raise SystemExit("Queue is empty")

slug = re.sub(r"[^a-z0-9]+", "-", item["title"].lower()).strip("-")
folder = pathlib.Path("pieces") / slug
folder.mkdir(parents=True, exist_ok=True)

(folder / "brief.md").write_text(
    f"# Brief\nAuthor: {q['author']} ({q['role']})\n"
    f"Date: {datetime.date.today()}\n\nInstruction:\n{item['instruction']}\n")

client = Anthropic()
msg = client.messages.create(
    model="claude-sonnet-5-5", max_tokens=8000,
    messages=[{"role": "user", "content": item["instruction"] +
      "\nUse public frameworks only. Original wording. "
      "Mark any placeholders clearly. Start with a note that this is an "
      "AI-assisted draft pending human review."}])
if msg.stop_reason == "max_tokens":
    raise RuntimeError(
        "Draft generation was truncated because the model reached the maximum output token limit."
    )
text = "\n".join(
    block.text
    for block in msg.content
    if getattr(block, "type", None) == "text"
    and hasattr(block, "text")
)

if not text.strip():
    raise RuntimeError("Anthropic returned no text content")
(folder / "draft.md").write_text(text)
(folder / "review.md").write_text(
    "# Review notes\nReviewed by:\nDate:\nChanges I made:\n"
)
item["status"] = "drafted"
yaml.safe_dump(q, open("queue.yml", "w"), sort_keys=False)
