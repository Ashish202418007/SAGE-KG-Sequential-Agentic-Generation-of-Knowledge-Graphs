fact_extraction_prompt = f"""
Extract all factual statements from this text as short, complete lines.

Rules:
- One fact per line containing all its support information. 
- The facts should be able to summarize or reason for events/facts in it.
- Keep all numbers, dates, names, amounts exactly as written.
- Include supporting details (context, conditions, specifications).
- No inference - only stated facts.

TEXT: {text}

Output each fact as a separate line.
"""

hierarchy_prompt = f"""
Analyze fact lines and plan triplet structure, no intermediate triplets required.

Tasks:
1. List all entity names (use exact names from source).
    - All numbers, names, dates, should be treated as separate entities with context identifiers etc.
    - No short forms, use exact names.
2. Identify which facts are compound (multiple relationships).
3. Plan how compound facts should be broken down and connect with atomic facts.
    - Use 1–2 step bridges between facts to preserve context.
    - Ensure connections across facts through shared entities.
    - The planning should be done in such a way that it is able to summarize or reason for events/facts in it.
4. Entity names must hold the descriptive details (phases, categories, types, levels, rounds, etc).
5. Predicates must stay **simple, generic verbs** (e.g., supports, awards, includes, requires, uses).
6. Ensure no contextual information (numbers, dates, monetary values) is lost in the plan.
7. Just give the plan, no triplets needed.

Input facts: {{previous_task_output}}

Output planning analysis only - no triplets yet.
"""

decomposition_prompt = f"""
Convert fact lines into atomic triplets using the planning analysis while preserving all contextual details and connections.

Rules:
- Strict format: (subject, predicate, object)
- Subjects/objects: carry the descriptive and contextual info (phases, rounds, categories, levels, amounts).
- Predicates: only simple linking verbs (supports, awards, includes, requires, uses).
- Every numerical or monetary value must be linked to its specific context.
- Ensure each fact from the plan is represented, no information omitted.
- Do not use underscores for subject, object.

**Pattern:**
Input: (entity, action, amount X for target Y in context Z)
Output:
- (entity, has_program, context Z program)
- (context Z program, has_amount, amount X)
- (context Z program, targets, target Y)

**IMPORTANT:**
- Output your final triplets in this EXACT format: (subject, predicate, object) with commas separating subject, predicate, and object.
- Ensure each triplet has exactly two commas, one after the subject and one after the predicate.
- Each triplet must be on a new line, enclosed in parentheses, with no trailing commas or spaces.

**Example Output:**
- (subject, has_program, context Z program)
- (context Z program, has_amount, amount X)
- (context Z program, targets, target Y)
"""