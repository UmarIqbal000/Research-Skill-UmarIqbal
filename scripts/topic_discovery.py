"""
Topic and Trend Discovery Engine
Fetches trending preprints from arXiv API, explores research domains,
and synthesizes structured topic briefs for academic research.
"""

import sys
import json
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from typing import Dict, List, Optional


TRENDING_DOMAINS = {
    "ai_agents": {
        "domain": "Artificial Intelligence & Autonomous Agents",
        "category": "cs.AI",
        "keywords": ["autonomous agents", "multi-agent coordination", "LLM reasoning", "tool-augmented learning"],
        "hot_topics": [
            "Decentralized Multi-Agent Verification and Consensus",
            "Self-Correcting Reasoning Loops in Long-Horizon Planning",
            "Resource-Constrained Agent Orchestration on Edge Hardware"
        ]
    },
    "machine_learning": {
        "domain": "Machine Learning & Deep Neural Architectures",
        "category": "cs.LG",
        "keywords": ["federated learning", "representation learning", "diffusion models", "state-space models"],
        "hot_topics": [
            "Communication-Efficient Federated Learning under Asymmetric Noise",
            "Structured State Space Duality for Sub-Quadratic Sequence Modeling",
            "Generalization Bounds for Over-Parameterized Diffusion Trajectories"
        ]
    },
    "distributed_systems": {
        "domain": "Distributed Systems & Cybersecurity",
        "category": "cs.DC",
        "keywords": ["byzantine fault tolerance", "consensus protocols", "edge computing", "zero-trust"],
        "hot_topics": [
            "Asynchronous Byzantine Consensus under Dynamic Network Partitions",
            "Energy-Optimal Workload Scheduling in Heterogeneous Fog Clusters",
            "Privacy-Preserving Provenance Tracking in Decentralized Storage"
        ]
    },
    "computational_biology": {
        "domain": "Computational Biology & Genomics",
        "category": "q-bio.BM",
        "keywords": ["protein conformation", "structural prediction", "single-cell RNA", "variant effect"],
        "hot_topics": [
            "Co-folding Dynamics of Flexible Protein-Ligand Interfaces",
            "Graph Neural Networks for Single-Cell Gene Regulatory Network Inference",
            "Generative Macromolecular Sequence Design with Physical Constraints"
        ]
    },
    "quantum_computing": {
        "domain": "Quantum Physics & Information Systems",
        "category": "quant-ph",
        "keywords": ["quantum error correction", "surface codes", "variational quantum algorithms"],
        "hot_topics": [
            "Fault-Tolerant Surface Code Decoding with Neural Decoders",
            "Mitigation of Barren Plateaus in Variational Quantum Eigensolvers",
            "Quantum State Tomography via Compressed Matrix Product Operators"
        ]
    }
}


def search_arxiv(query: str, max_results: int = 5) -> List[Dict[str, str]]:
    """Search arXiv API for relevant preprints."""
    base_url = "http://export.arxiv.org/api/query?"
    params = {
        "search_query": f"all:{query}",
        "start": 0,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending"
    }
    url = base_url + urllib.parse.urlencode(params)
    
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "ResearchEcosystem/1.0"})
        with urllib.request.urlopen(req, timeout=10) as response:
            content = response.read().decode("utf-8")
            
        root = ET.fromstring(content)
        namespace = {"atom": "http://www.w3.org/2005/Atom"}
        
        results = []
        for entry in root.findall("atom:entry", namespace):
            title = entry.find("atom:title", namespace)
            summary = entry.find("atom:summary", namespace)
            published = entry.find("atom:published", namespace)
            id_url = entry.find("atom:id", namespace)
            
            clean_title = title.text.strip().replace("\n", " ") if title is not None else "Untitled"
            clean_summary = summary.text.strip().replace("\n", " ") if summary is not None else ""
            pub_date = published.text[:10] if published is not None else "Unknown"
            paper_id = id_url.text.split("/abs/")[-1] if id_url is not None else ""
            
            authors = []
            for author in entry.findall("atom:author", namespace):
                name = author.find("atom:name", namespace)
                if name is not None:
                    authors.append(name.text)
            
            results.append({
                "id": paper_id,
                "title": clean_title,
                "authors": authors[:3],
                "date": pub_date,
                "abstract": clean_summary[:300] + "..." if len(clean_summary) > 300 else clean_summary
            })
        return results
    except Exception as e:
        return [{"error": f"arXiv query failed: {str(e)}"}]


def get_trending_domains() -> Dict[str, Dict]:
    """Return catalog of trending research domains and active frontier topics."""
    return TRENDING_DOMAINS


def synthesize_topic_brief(topic_or_keyword: str, difficulty: str = "medium") -> Dict[str, str]:
    """Generate a structured research topic brief."""
    papers = search_arxiv(topic_or_keyword, max_results=3)
    
    brief = {
        "working_title": f"Advancing {topic_or_keyword.title()}: Methodological Foundations and Empirical Analysis",
        "domain": "Cross-Disciplinary Applied Sciences",
        "difficulty_tier": difficulty.lower(),
        "core_problem": f"Current approaches to {topic_or_keyword} face trade-offs between computational efficiency, robustness, and theoretical guarantees.",
        "proposed_mechanism": f"An adaptive framework coupling localized parameter optimization with provable convergence bounds.",
        "preliminary_references": [p.get("title", "") for p in papers if "error" not in p]
    }
    return brief


if __name__ == "__main__":
    if len(sys.argv) > 1:
        query = sys.argv[1]
        print(f"Searching arXiv for: {query}")
        results = search_arxiv(query, max_results=3)
        print(json.dumps(results, indent=2))
    else:
        print("Available Trending Domains:")
        print(json.dumps(get_trending_domains(), indent=2))
