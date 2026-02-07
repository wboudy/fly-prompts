# Contributing to fly-prompts

## 🔧 Prompt Engineering Guidelines

When updating or creating prompts in this library, follow these principles:

### 1. Be explicit, not implicit
State exactly what you want — format, length, tone, audience. Don't make the model guess.

### 2. Use structured delimiters
Wrap variable inputs in XML tags (e.g., `<context>`, `<instructions>`) so the model can clearly distinguish sections.

### 3. Front-load critical instructions
Put the most important constraints and identity framing at the top. Models attend more strongly to the beginning and end.

### 4. Give examples
Even one good input/output pair (few-shot) dramatically improves consistency. Show, don't just tell.

### 5. Specify what NOT to do
Negative constraints ("Do not include disclaimers," "Avoid bullet points") are surprisingly effective guardrails.

### 6. Control output format explicitly
If you need JSON, markdown, a specific schema — define it in the prompt and consider asking the model to think step-by-step before producing the final output.

### 7. Keep system prompts and user prompts distinct
System = identity, rules, tone. User = the task. Don't blur them.

### 8. Test edge cases
After writing a prompt, mentally (or actually) run adversarial inputs through it. If it breaks easily, add constraints.

---

## Tone

**Professional, concise, reusable.** Every prompt should work as a reliable template, not a one-off.

---

## Structure

Each prompt should include:

- `<instructions>` — What the agent should do
- `<steps>` — Numbered steps if procedural
- `<example>` — At least one concrete example
- `<constraints>` — What NOT to do
- `<output_format>` — Expected output structure (if applicable)

## Submitting Changes

1. Fork the repo
2. Create a branch for your changes
3. Follow the guidelines above
4. Test your prompts with actual agents if possible
5. Submit a PR with a clear description
