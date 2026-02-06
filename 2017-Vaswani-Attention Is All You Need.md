# Paper Summary: Attention Is All You Need

**ArXiv ID:** 1706.03762  
**Authors:** Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Łukasz Kaiser, Illia Polosukhin  
**Published:** 2017 (NeurIPS 2017)

---

## 1. Main Idea

The paper proposes the **Transformer**, a revolutionary neural network architecture for sequence transduction (e.g., machine translation) that **completely eliminates recurrence and convolution**. Instead, the model relies **entirely on attention mechanisms** to compute representations and draw global dependencies between input and output sequences.

The core motivation is to overcome the fundamental limitation of recurrent neural networks (RNNs, LSTMs, GRUs): their **inherently sequential nature** prevents parallelization within training examples. As sequence lengths increase, this sequential constraint becomes a critical bottleneck. The Transformer allows for significantly more parallelization while achieving superior quality in less training time.

---

## 2. Main Novelty

The paper introduces several key innovations:

### 2.1 Self-Attention Architecture
- **First transduction model** that computes representations of input and output entirely using self-attention
- No sequence-aligned RNNs or convolutional layers
- Connects all positions with a constant number of sequentially executed operations

### 2.2 Scaled Dot-Product Attention
Formula: `Attention(Q, K, V) = softmax(QK^T / √d_k)V`

- The scaling factor `1/√d_k` counteracts the effect of dot products growing large in magnitude for high-dimensional keys (which pushes softmax into regions with extremely small gradients)
- More efficient than additive attention (uses highly optimized matrix multiplication)

### 2.3 Multi-Head Attention
- Parallel attention mechanisms (h = 8 heads) with different learned linear projections
- Allows the model to jointly attend to information from different representation subspaces at different positions
- Each head uses d_k = d_v = d_model/h = 64 dimensions

### 2.4 Encoder-Decoder Architecture
- **Encoder:** Stack of N=6 identical layers, each with:
  1. Multi-head self-attention
  2. Position-wise feed-forward network
- **Decoder:** Stack of N=6 identical layers with additional encoder-decoder attention
- Residual connections and layer normalization throughout

### 2.5 Sinusoidal Positional Encoding
- Since the model has no recurrence or convolution, positional encodings are added to input embeddings
- Uses sine and cosine functions of different frequencies to allow the model to learn relative positions

### 2.6 Key Advantages over RNNs/CNNs

| Layer Type | Complexity per Layer | Sequential Operations | Max Path Length |
|------------|---------------------|----------------------|-----------------|
| Self-Attention | O(n² · d) | O(1) | O(1) |
| Recurrent | O(n · d²) | O(n) | O(n) |
| Convolutional | O(k · n · d²) | O(1) | O(log_k(n)) |

---

## 3. Main Datasets Used for Evaluation

### 3.1 Machine Translation Tasks

#### WMT 2014 English-to-German (EN-DE)
- **Size:** ~4.5 million sentence pairs
- **Vocabulary:** ~37,000 tokens (shared source-target)
- **Tokenization:** Byte-pair encoding (BPE)

#### WMT 2014 English-to-French (EN-FR)
- **Size:** 36 million sentences
- **Vocabulary:** 32,000 word-piece vocabulary
- **Significantly larger dataset than EN-DE**

### 3.2 English Constituency Parsing (Generalization Test)

#### Wall Street Journal (WSJ) - Penn Treebank
- **Size:** ~40,000 training sentences
- **Vocabulary:** 16K tokens
- **Purpose:** Test if Transformer generalizes to other tasks

#### Semi-supervised Setting
- **Additional Data:** High-confidence and BerkleyParser corpora
- **Size:** ~17 million sentences
- **Vocabulary:** 32K tokens

---

## 4. Experimental Procedure

### 4.1 Hardware Configuration
- **GPUs:** 8 NVIDIA P100 GPUs on a single machine
- **Training Duration:**
  - Base model: 100,000 steps (~12 hours)
  - Big model: 300,000 steps (~3.5 days)

### 4.2 Training Configuration

#### Batch Processing
- Sentence pairs batched by approximate sequence length
- Each batch: ~25,000 source tokens + ~25,000 target tokens

#### Optimizer
- **Adam** optimizer with:
  - β₁ = 0.9
  - β₂ = 0.98
  - ε = 10⁻⁹

#### Learning Rate Schedule
```
lrate = d_model^(-0.5) · min(step_num^(-0.5), step_num · warmup_steps^(-1.5))
```
- Linear warmup for first 4,000 steps
- Then decrease proportionally to inverse square root of step number

#### Model Hyperparameters (Base Model)
| Parameter | Value |
|-----------|-------|
| N (layers) | 6 |
| d_model | 512 |
| d_ff (feed-forward dim) | 2048 |
| h (attention heads) | 8 |
| d_k, d_v | 64 |
| Dropout | 0.1 |
| Label smoothing | 0.1 |

#### Regularization
1. **Residual Dropout:** P_drop = 0.1 applied to:
   - Output of each sub-layer
   - Sums of embeddings and positional encodings
2. **Label Smoothing:** ε_ls = 0.1 (improves accuracy and BLEU at cost of perplexity)

### 4.3 Inference Procedure

#### Checkpoint Averaging
- Base models: Average last 5 checkpoints (written at 10-minute intervals)
- Big models: Average last 20 checkpoints

#### Beam Search
- Beam size: 4
- Length penalty: α = 0.6
- Max output length: input length + 50 (with early termination)

### 4.4 Key Results

| Task | Model | BLEU | Training Cost (FLOPs) |
|------|-------|------|----------------------|
| EN-DE | Transformer (big) | **28.4** | 2.3×10¹⁹ |
| EN-FR | Transformer (big) | **41.8** | 9.6×10¹⁸ |

- EN-DE: Outperformed all previous models (including ensembles) by >2.0 BLEU
- EN-FR: New single-model state-of-the-art at <1/4 the training cost of previous SOTA
- Training time: Only 3.5 days on 8 P100 GPUs vs. weeks/months for competing models

### 4.5 Ablation Studies (Newstest2013 Development Set)

The paper systematically tested variations:
- **Attention heads:** 8 heads optimal (single head: -0.9 BLEU)
- **Attention key dimension:** Larger d_k improves quality
- **Model size:** Bigger models perform better (as expected)
- **Dropout:** Essential for avoiding overfitting
- **Positional encoding:** Learned embeddings ≈ sinusoidal (nearly identical results)

### 4.6 Generalization Test (Constituency Parsing)
- 4-layer Transformer adapted with minimal changes
- Trained on WSJ only and semi-supervised settings
- **Results:** Better than BerkeleyParser even with limited (40K) training data; competitive with RNN Grammar in semi-supervised setting
- **Finding:** Model generalizes well to tasks with structural constraints and longer outputs

---

## 5. Impact and Significance

The Transformer architecture has become the foundation for modern NLP:
- **BERT** (Devlin et al., 2018) - bidirectional encoder
- **GPT** series (Radford et al.) - autoregressive decoder
- **Vision Transformers** (ViT) - applied to computer vision
- **Modern LLMs** - GPT-3, GPT-4, Claude, and virtually all large language models use the transformer architecture

The paper's key insight — that attention alone is sufficient for sequence modeling — fundamentally changed the field, enabling:
- Massive parallelization during training
- Better handling of long-range dependencies (O(1) path length)
- Scalability to much larger models and datasets
