# SAGE-KG: A Multi-Agent Framework for Automatic Knowledge Graph Construction

SAGE-KG is an unsupervised, zero-shot multi-agent system designed to transform unstructured text into high-quality knowledge graphs (KGs) without relying on proprietary models, predefined schemas, or domain-specific fine-tuning. It provides a scalable, accessible, and modular approach to knowledge graph construction suitable for retrieval-augmented generation (RAG), reasoning tasks, and complex information extraction.

## Overview

Large language models (LLMs) excel at reasoning and generation but remain susceptible to hallucinations when their internal knowledge is incomplete or outdated. While RAG systems mitigate this by grounding model outputs in external data, traditional vector-store-based RAG struggles with multi-relational reasoning and complex fact linking.

Knowledge graphs address these limitations by encoding entities and relationships in a structured format. However, existing KG construction frameworks often depend on proprietary LLMs, brittle schemas, or heavy fine-tuning.

SAGE-KG eliminates these constraints through a three-agent pipeline powered by small, open-source language models.

## Key Features

* **Fully Unsupervised and Zero-Shot:** No fine-tuning, labeling, or schema engineering required.
* **Small Open-Source Models:** Utilizes Qwen2.5-family models for cost efficiency, reproducibility, and accessibility.
* **Three-Step Agentic Pipeline:**

  * **Fact Extractor:** Parses raw text into explicit, entity-repeated factual statements.
  * **Schema Planner:** Normalizes entities, decomposes statements, and plans relation structures.
  * **Triplet Creator:** Produces consistent, standardized (subject, predicate, object) triplets.
* **Domain Agnostic:** Works across scientific, biographical, technical, and general domains.
* **Modular Architecture:** Easily integrates with different LLMs, vector stores, KG databases, or RAG systems.
* **High-Quality Triplets:** Maintains fine-grained relational detail without clustering or context loss.

## Motivation

Traditional RAG pipelines built on text embeddings perform well for simple lookups but fall short for multi-hop reasoning and complex relational tasks. Structured retrieval approaches such as GraphRAG, KGGen, and AutoSchemaKG have advanced the space but frequently suffer from:

* Dependence on proprietary foundation models
* High computational cost and low reproducibility
* Schema rigidity
* Loss of relational specificity through clustering or summarization

SAGE-KG addresses these issues by offering a fully open, reproducible, lightweight system for high-fidelity KG construction.

## Architecture

The SAGE-KG workflow comprises three sequential agents:

1. **Fact Extractor**

   * Converts raw text into explicit factual statements
   * Repeats entity names to preserve connectivity and avoid entity isolation

2. **Schema Planner**

   * Ensures entity consistency
   * Decomposes compound statements
   * Designs a structured plan mapping each fact to a clean triplet format

3. **Triplet Creator**

   * Generates standardized (subject, predicate, object) triplets
   * Ensures deterministic, reproducible output
   * Produces domain-independent KG representations

### Example Output

```
(Liam Thomas Garrigan, has birth date, 17 October 1981)  
(Liam Thomas Garrigan, has nationality, English)
(Liam Thomas Garrigan, has profession, Actor)
```

## Getting Started

### Installation

Clone the repository:

```bash
git clone https://github.com/Ashish202418007/SAGE-KG-Sequential-Agentic-Generation-of-Knowledge-Graphs.git
cd SAGE-KG
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To run the full SAGE-KG pipeline on a folder of Markdown files, use the command-line interface below. The script loads an Ollama model, processes all documents in the specified directory, and outputs the resulting triplets in both JSON and TXT formats.

### Command

```bash
python Agents.py \
    --data-folder data \
    --model qwen2.5:14b \
    --output-json triplets.json \
    --output-txt triplets.txt
```

### Arguments

| Argument        | Description                                                        | Default         |
| --------------- | ------------------------------------------------------------------ | --------------- |
| `--data-folder` | Path to folder containing input Markdown files for extraction      | `data`          |
| `--model`       | Ollama model name to use (passed as `ollama/<model>`)              | `qwen2.5:14b`   |
| `--output-json` | Output file containing all extracted triplets in JSON format       | `triplets.json` |
| `--output-txt`  | Output file containing all extracted triplets in plain text format | `triplets.txt`  |

### Execution Flow

The entrypoint (`main()`) performs the following steps:

1. Parses command-line arguments.
2. Initializes the Ollama-backed LLM:

   ```python
   llm = ChatOllama(model=f"ollama/{args.model}", temperature=0)
   ```
3. Instantiates the `TripleProcessor` with the selected model and data directory.
4. Executes the full extraction and triplet-generation pipeline:

   ```python
   processor.run()
   ```
5. Writes results to both JSON and TXT outputs.

After processing completes, the script prints:

```
Processing completed!
```

### Example Folder Structure

```
SAGE-KG/
  data/
    doc1.md
    doc2.md
  Agents.py
  triplets.json
  triplets.txt
```

This setup enables fully automated multi-agent triplet extraction across an entire directory of source documents.


## Applications

* Knowledge graph construction
* Graph-based RAG
* Multi-hop reasoning
* Information extraction pipelines
* Scientific literature analysis
* Enterprise document structuring


## Contributing

Contributions are welcome. Please open an issue or submit a pull request for enhancements, bug fixes, or feature suggestions.

---

SAGE-KG enables reproducible, scalable, and schema-free knowledge graph construction using only open-source tools, supporting the next generation of trustworthy reasoning systems.
