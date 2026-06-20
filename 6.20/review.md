#### 简单问题：
编号	问题
Q1	Who are the authors of this paper?
- Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Łukasz Kaiser, and Illia Polosukhin.
Q2	What is the title of this paper?
- Attention Is All You Need.
Q3	What is Transformer?
- Transformer is a sequence transduction model based entirely on attention mechanisms, without recurrence or convolution.
Q4	What problem does the paper address?
-  The paper addresses sequence transduction tasks such as machine translation, aiming to improve efficiency and modeling of long-range dependencies. 

#### 中等问题
编号	问题
Q5	How many attention heads are used in the base model?
- 8 attention heads.
Q6	What is the value of d_model in the base Transformer?
- d_model = 512.
Q7	What optimizer is used in this paper?
-  Adam optimizer.
Q8	What datasets are used for evaluation?
- WMT 2014 English-to-German and WMT 2014 English-to-French translation datasets.
Q9	What is the dimension of the feed-forward layer in the base model?
- d_ff = 2048.

#### 困难问题
编号	问题
Q10	What value of label smoothing is used during training?
- ε_ls = 0.1 (label smoothing value is 0.1).
Q11	What are the β1 and β2 values of the Adam optimizer?
- β1 = 0.9, β2 = 0.98 (ε = 10^-9).
Q12	What warmup steps are used in the learning rate schedule?
- 4000 warmup steps.
Q13	What dropout rate is used in the Transformer model?
-  Dropout rate = 0.1.
Q14	By how much did the Transformer improve BLEU score on English-to-German translation?
- The base Transformer achieved 27.3 BLEU, improving over previous best models by more than 2 BLEU points.
Q15	What beam size is used during inference?
- Beam size = 4.

#### 未包含问题
编号	问题
Q16	What operating system was used during training?
Q17	What reinforcement learning algorithm was used?
Q18	What is the GitHub repository URL for this work?


##### 评分标准：
- 1分：完全正确
- 0.5分：部分正确，但是有遗漏或小错误
- 0分：错误，或者没回答出关键信息


**Exp1：**
chunk_size=300
chunk_overlap=50
k=3
------
Question	Score   Answer
Q1          0.5     The authors of this paper are Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, and Aidan N. Gomez.
Q2	        1       The title of the paper is "Attention Is All You Need."
Q5	        1       8
Q6	        1       512
Q7          1       The optimizer used in this paper is Adam.
Q10	        1       0.1
Q11	        1       The β₁ value is **0.9** and the β₂ value is **0.98**.
Q12	        1       The warmup steps used in the learning rate schedule are **4000**.
Q16	        1       The information provided does not specify the operating system used during training.      
Q17         1       No reinforcement learning algorithm was used.                

**Exp2：**
chunk_size=500
chunk_overlap=100
k=3
------
Question	Score   Answer	
Q1	        0.5     - Ashish Vaswani - Noam Shazeer - Niki Parmar - Jakob Uszkoreit - Llion Jones - Aidan N. Gomez
Q2	        0       The title of this paper is Google’s neural machine translation system: Bridging the gap between human and machine translation.
Q5	        1       The base model uses 8 attention heads.
Q6	        1      \boxed{512}
Q7          1       $\boxed{\text{Adam}}$
Q10	        1       0.1
Q11	        1       β₁ = 0.9  β₂ = 0.98
Q12	        1       The warmup steps used in the learning rate schedule are **4000**.
Q16	        0       Linux
Q17         1       The text does not specify a reinforcement learning algorithm; it focuses on optimization and model training details instead.

**Exp3：**
chunk_size=1000
chunk_overlap=200
k=3
------
Question	Score   Answer
Q1          0.5     包含了参考文献的作者 These authors contributed to various works cited in the provided references, which cover topics such as neural machine translation, recurrent models, and efficient parsing systems.
Q2	        0       The title of the paper is "Effective self-training for parsing."
Q5	        1       The base model uses \boxed{8} attention heads.
Q6	        1       The value of d_model in the base Transformer is **512**.
Q7          1       The optimizer used in this paper is the Adam optimizer.
Q10	        1       $\boxed{0.1}$
Q11	        1       β₁ = 0.9，β₂ = 0.98
Q12	        1       The warmup steps used in the learning rate schedule are **4000**.
Q16	        0       The operating system used during training was Linux.
Q17         1       文中并未提及使用任何强化学习算法。


##### 错误分析：
第一组回答准确率是95%，第二组和第三组分别都是75%。
对于这三组而言，论文的作者比较难判断，参考文献的不知道要不要包含，列举但列举不完全都是可能出现的情况。
对于后两组参数而言，论文的标题难以判断。这说明参数设置会影响关键文本块的检索质量，尤其是对于一些较短的关键文本块。不合理的文本切分策略很可能导致论文无法识别关键的文本块。
论文中并没有提到操作系统是Linux，但是第二组和第三组模型都根据常识猜测出了Linux这个答案，检索结果中并没有答案，但是模型却没有回答不知道，这说明rag缺乏有效的拒绝回答的机制，检索失败时容易产生幻觉。