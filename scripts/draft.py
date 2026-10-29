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

prompt = (
    item["instruction"]
    + "\nUse public frameworks only. Use original wording. "
    + "Mark any placeholders clearly. "
    + "Start the document with: "
    + "'DRAFT – PENDING HUMAN REVIEW AND ORGANISATIONAL APPROVAL'. "
    + "Do not state or imply that the document has been formally approved, "
    + "certified, accredited or adopted by an organisation. "
    + "Produce a complete but concise document. "
    + "Prioritise complete coverage of every requested section over lengthy explanation. "
    + "Use concise tables, bullet points and short paragraphs where appropriate. "
    + "Do not repeat information unnecessarily."
)
messages = [{"role": "user", "content": prompt}]
parts = []

for attempt in range(3):
    msg = client.messages.create(
        model="claude-sonnet-5-5",
        max_tokens=8000,
        messages=messages,
    )

    chunk = "\n".join(
        block.text
        for block in msg.content
        if getattr(block, "type", None) == "text"
        and hasattr(block, "text")
    )

    if chunk:
        parts.append(chunk)

    if msg.stop_reason == "end_turn":
        break

    if msg.stop_reason == "max_tokens":
        full_text = "\n".join(parts)

        messages = [
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": full_text},
            {
                "role": "user",
                "content": (
                    "Continue exactly from where you stopped. "
                    "Complete all remaining requested sections. "
                    "Do not repeat sections already written. "
                    "Finish the document properly."
                ),
            },
        ]
        continue

    raise RuntimeError(
        f"Draft generation stopped unexpectedly: {msg.stop_reason}"
    )

else:
    raise RuntimeError(
        "Draft generation was still incomplete after 3 generation attempts."
    )

text = "\n".join(parts)

if not text.strip():
    raise RuntimeError("Anthropic returned no text content")
(folder / "draft.md").write_text(text)
(folder / "review.md").write_text(
    "# Review notes\nReviewed by:\nDate:\nChanges I made:\n"
)
item["status"] = "drafted"
yaml.safe_dump(q, open("queue.yml", "w"), sort_keys=False)
