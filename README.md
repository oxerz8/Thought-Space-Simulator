# Thought-Space-Simulator
Visualize and explore the dynamics of human thought as a 3D network of interconnected ideas.

The Thought Space Simulator models thoughts as nodes in a network, where each thought has attributes like awareness, intensity, and recursiveness. Thoughts can influence one another, evolve over time, and collapse into definite states as they become more “aware.”

<img width="820" height="562" alt="image" src="https://github.com/user-attachments/assets/ec3bb429-4812-44ef-970c-bd39b1f9dca5" />

The position of a thought is calculated by using a Large Language Model (LLM) to determine the recursiveness, intensity, and awareness of a thought phrase.  
Hence,  
$$T = f(Awareness, Intensity, Recursion)$$

# Features

## Thought Nodes
Each thought is represented as a node with:

- **Awareness** – clarity or insight level  
- **Intensity** – how strong or active the thought is  
- **Recursion** – how much it reflects on itself  
- **Concept** – the main theme of the thought  
- **State** – superposed (potential) or collapsed (definite)  

## Dynamic Influence
Thoughts spread intensity to connected neighbors, simulating how ideas reinforce each other in a network.

## 3D Interactive Visualization
Explore the thought space in 3D using Plotly, with nodes color-coded by concept and edges representing logical connections.

## ML-Powered Thought Rating
Each thought is automatically rated for awareness, intensity, recursion, and concept using a language model, enabling dynamic simulation.

## Flexible Input
Input your own set of thoughts as text lines to generate a personalized thought network.

# How It Works

## Thought Creation
Each input phrase is converted into a ThoughtNode and rated using a language model for awareness, intensity, recursion, and concept.

## Edge Creation
Thoughts are connected based on logical relationships evaluated by the LLM. Edge weights currently use random values but can be extended to semantic similarity.

## Dynamic Simulation
Each simulation step:

- Collapses thoughts with high awareness into definite states.  
- Spreads intensity to connected neighbors to simulate cognitive influence.  

## 3D Visualization
Nodes are placed using a spring layout in 3D space. Hover over nodes to see their properties.

# Future Improvements

- Use semantic embeddings to determine edge weights more meaningfully.  
- Incorporate contradiction or conflict metrics to model cognitive dissonance.  
- Allow real-time interaction and addition of thoughts.  
- Export thought networks for further analysis or integration with AI models.  

# References / Inspirations

The design of thought node dimensions is based on a combination of philosophical, cognitive, and computational ideas:

## Awareness
- Inspired by Global Workspace Theory (Baars, 1988), which models conscious access and attention.  
- Reflects the clarity or insight of a thought in your simulator.

## Intensity
- Based on concepts of neural activation and cognitive salience, capturing how strong or emotionally charged a thought is.  
- Influences the spread of ideas through the thought network.
- Inspired by William James(1890). His work inspired the idea that thoughts have intensity and awareness, and that they influence each other in a network-like fashion.

## Recursion
- Derived from metacognition and self-reflective reasoning in philosophy and cognitive science.  
- Represents nested or self-referential thought patterns.
- Chomsky called recursion the defining feature of language.

## Contradiction (optional / simplified)
- Inspired by cognitive dissonance theory (Festinger, 1957) and philosophical discussions on paradoxes and logical conflict.  
- Measures internal conflict or instability in a thought.

## Concept
- Adapted from semantic clustering and topic modeling in NLP.  
- Represents the core theme or category of the thought.

## General Approach
- The network dynamics are influenced by ideas from graph theory, complex systems, and LLM-based semantic evaluation.  
- Node interactions model influence and propagation of ideas in a simplified cognitive space.

## References
- Baars, B. J. (1988). *A Cognitive Theory of Consciousness*. Cambridge University Press.  
- Festinger, L. (1957). *A Theory of Cognitive Dissonance*. Stanford University Press.  
- Global Workspace Theory: https://www.scholarpedia.org/article/Global_workspace_theory  
- Sentence embeddings / semantic clustering inspiration: Reimers, N., & Gurevych, I. (2019). *Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks*.  

# License
This project is released under the MIT License.
