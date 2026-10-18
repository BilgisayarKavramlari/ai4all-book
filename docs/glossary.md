# Glossary

One entry per term. Keep definitions short and identical wherever the term is defined in the book. Turkish equivalent in the third column for the later Turkish edition.

| Term | Definition | Türkçe |
|---|---|---|
| Large language model (LLM) | A generative model that produces text, trained on large amounts of text to predict the next token in a sequence. | Büyük dil modeli |
| Token | A unit of text (a word, part of a word, or a symbol) that a language model receives and produces. | Belirteç (token) |
| Hallucination | Fluent output that is not supported by the model's input or by facts. | Halüsinasyon / uydurma |
| Generative AI system | Software that produces new content, such as text, images or code, in response to an input. | Üretken yapay zekâ |
| Prompt | The input you give an AI tool. | İstem |
| Output | What an AI tool produces in response to a prompt. | Çıktı |
| Model | A set of learned settings (parameters) that turns an input into an output; in an AI tool, the part that produces the output from your prompt. (Informal in Ch. 1, formal in Ch. 2.) | Model |
| Jagged technological frontier | The uneven boundary between tasks an AI tool handles well and tasks it handles poorly, even among tasks that look equally hard. | Pürüzlü teknolojik sınır |
| AI Work Loop | The book's five-step method for AI-assisted work: Frame, Prompt, Verify, Decide, Disclose. | Yapay zekâ çalışma döngüsü |
| AI Use Declaration | A short statement of which AI tools you used, for what, what you accepted, rejected or revised, how you verified it, and where your judgment shaped the work. | Yapay zekâ kullanım beyanı |
| Assistance | AI use that helps you do the thinking yourself. | Destek (yardım) |
| Outsourcing | AI use that replaces the thinking an assignment or task requires of you. | Dış kaynak kullanımı (devretme) |
| Overconfidence | Output stated with more certainty than the evidence supports. | Aşırı güven |
| Productivity (in a study) | A defined measure of output per unit of time, such as issues resolved per hour. | Verimlilik |
| Staggered rollout | Introducing a tool to groups at different times, which lets researchers compare groups with and without it. | Kademeli kullanıma sunma |
| Difference-in-differences | A method that compares the change in one group with the change in a comparison group over the same period. | Farkların farkı |
| Control group | In an experiment, the comparison group that does not receive the tool or treatment. | Kontrol grubu |
| Random assignment | Using chance to decide who receives a tool, so groups are alike on average in everything else. | Rastgele atama |
| Percentage point | The simple difference between two percentages (for example, 84% minus 65% is 19 percentage points). | Yüzde puan |
| Fluent (output) | Smooth, confident, well-organized text that sounds expert, whether or not it is correct. | Akıcı (çıktı) |
| Baseline | An honest record of how you use AI at the start of the course, used to measure your progress. | Başlangıç düzeyi |
| Outdated information | Output that was once correct but no longer is, because of a training-data cutoff or stale search results. | Güncelliğini yitirmiş bilgi |
| Rule-based system | A system that follows rules written by people. | Kural tabanlı sistem |
| Machine learning | The part of AI in which a system finds rules (patterns) from examples instead of having them written by people. | Makine öğrenmesi |
| Training data | The examples a model learns from. | Eğitim verisi |
| Example | One item in a dataset, such as one photo or one email. | Örnek |
| Feature | A measurable property of an input that a model uses, such as a pixel value or a house's size. | Öznitelik |
| Label | The correct answer attached to an example: a human decision or a recorded outcome. | Etiket |
| Supervised learning | Learning from examples that each come with a correct answer (label). | Gözetimli öğrenme |
| Error | How far a model's prediction is from the correct answer. | Hata |
| Inference | Using a trained model to produce an output for a new input. | Çıkarım |
| Sample | The examples we actually have. | Örneklem |
| Population | Everything a model will meet in the real world. | Evren (popülasyon) |
| Sampling bias | A systematic difference between the sample and the population. | Örnekleme yanlılığı |
| Proxy | A clue that stands in for something else, such as a word linked to gender. | Vekil değişken |
| Noisy labels | Labels that are wrong at random, in no particular direction. | Gürültülü etiketler |
| Biased labels | Labels that are wrong in one consistent direction, often because they record past decisions. | Yanlı etiketler |
| Class imbalance | When one class has far fewer examples than the others. | Sınıf dengesizliği |
| Shortcut | A clue that goes with the label in the training data but is irrelevant to the task. | Kestirme (kısa yol) öğrenme |
| Overfitting | When a model fits its training examples so closely that it stops improving, or gets worse, on new examples. | Aşırı öğrenme (ezberleme) |
| Training set | The labeled examples used to train a model. | Eğitim kümesi |
| Test set | Labeled examples kept away from training and used only to score the model. | Test kümesi |
| Deep learning | Machine learning with many layers of simple computing units. | Derin öğrenme |
| Data-to-Prediction Pipeline | The book's five-stage picture of how data becomes predictions: collect, label, train, predict, feedback. | Veriden tahmine hattı |
| Datasheet (for a dataset) | A document that records why a dataset was created, what it contains, how it was collected and labeled, and what it should not be used for (after Gebru et al., 2021). | Veri seti bilgi formu |
| Gradient descent | A training method that changes a model's settings in small steps that reduce the error. | Gradyan inişi |
| Precision | Of the cases a model flagged, the share that were really positive. | Kesinlik |
| Recall | Of the real cases of a class, the share the model caught (the score on the smallest class in Ch. 2). | Duyarlılık (geri çağırma) |
| Discriminative model | A model that learns the boundary between classes. | Ayırt edici model |
| Class | One of the possible answers a classifier can give, such as "bolt" or "nut". | Sınıf |
| Parameter | One of the learned settings inside a model; training adjusts parameters. | Parametre |
| Self-supervised learning | Learning from examples whose answer is hidden in the data itself, such as the next word in a sentence. | Öz-denetimli öğrenme |
| Learning rate | The size of each adjustment step in gradient descent. | Öğrenme oranı |
| Generative AI | AI that produces new content (text, images, audio or code); today built almost entirely with deep learning. | Üretken yapay zekâ |
| Tokenizer | A program that splits text into tokens and gives each token a number. | Belirteçleyici (tokenizer) |
| Probability distribution | A set of chances for all possible outcomes that add up to 100%. | Olasılık dağılımı |
| Sampling (of tokens) | Picking the next token according to the model's scores (not the same as a sample of examples in Chapter 2). | Örnekleme (belirteç seçimi) |
| Next-token prediction | Producing text one token at a time in four steps: split the text into tokens, score every possible next token, pick one, add it and repeat. | Sonraki belirteç tahmini |
| Reasoning tokens | Extra tokens some tools produce before the answer, sometimes hidden; they are made in the same way as other tokens and count toward context and cost. | Akıl yürütme belirteçleri |
| Option | A control a user can change, such as temperature or search on or off; unlike the model's settings (parameters), it is not learned. | Seçenek |
| Temperature | An option that changes how often less likely tokens are picked; it does not change the model's settings. | Sıcaklık (sıcaklık seçeneği) |
| Pretraining | The first stage of training a language model: self-supervised learning on very large collections of text, in which the settings are adjusted so that the real next token gets a higher score. | Ön eğitim |
| Fine-tuning | Extra training of an already trained model on a smaller, new set of texts or examples. | İnce ayar |
| Instruction tuning | Further training on prompts paired with good responses written by people. | Talimat ayarı (talimatla ince ayar) |
| Learning from human feedback | A training stage in which people rank responses, a separate scoring model is trained on their rankings, and the settings move toward responses that score higher. | İnsan geri bildiriminden öğrenme |
| Knowledge cutoff | The date after which no text was collected for a model's training. | Bilgi kesim tarihi |
| Context window | The space for everything a language model receives in one turn, measured in tokens; the response also counts toward it. | Bağlam penceresi |
| System prompt | Instructions from a tool's provider or developer that are added to the context window, usually unseen by the user. | Sistem istemi |
| Memory (product feature) | A product feature that saves notes about a user, or draws on past chats, and adds them to later conversations; it adds text and does not train the model. | Bellek (ürün özelliği) |
| Retrieval | A system's search of a collection, such as the web or a set of files, that adds the passages it finds to the context window. | Erişim (getirme) |
| Retrieval-augmented generation (RAG) | Producing a response with retrieved passages added to the context window. | Erişimle zenginleştirilmiş üretim |
| Tool use | A model producing a request to run other software, such as a calculator or a search engine, whose result is added to the context window. | Araç kullanımı |
| Agent | A system in which the model directs its own steps and tool use toward a goal; in a workflow, people fixed the steps in advance (adapted from Anthropic, 2024). Not the same as the AI Fluency "agency" mode. | Ajan (yapay zekâ ajanı) |
| Probe | A small test of a model's behavior with four parts: prediction, prompt, result and conclusion. | Yoklama (sınama) |
| Reversal curse | The finding that a model trained on "A is B" often fails to answer "B is A" (Berglund et al., 2024). | Tersine çevirme laneti |
| Attention (Deep) | In a Transformer, the mechanism that updates each token's representation with a weighted mix of the tokens before it. | Dikkat (mekanizması) |
| Transformer (Deep) | The model architecture, introduced in 2017, on which most of today's large language models are built (as of October 2026). | Transformer (dönüştürücü mimarisi) |
| Failure (AI) | An output or action of an artificial intelligence (AI) system that does not do what the task needs. | Başarısızlık (yapay zekâ hatası) |
| Failure Taxonomy Tree | The book's diagram that sorts AI failures into five branches, each with smaller leaves. | Başarısızlık sınıflandırma ağacı |
| Bias (in generated output) | A systematic pattern in outputs that treats or represents people or groups unfairly. | (Üretilen çıktıda) yanlılık |
| Context loss | Output that ignores information or instructions the model was given. | Bağlam kaybı |
| Security vulnerability (AI) | A weakness that lets someone make an AI system act against its owner's intent or reveal what it should not. | Güvenlik açığı |
| Documented (label) | A failure label for which the evidence shows the branch's defining feature. | Belgelenmiş (etiket) |
| Inferred (label) | A failure label for which the evidence does not show the branch's defining feature; drawn with a dashed border. | Çıkarsanmış (etiket) |
| Intrinsic hallucination | A hallucination that contradicts the input the model received: what you pasted, or what the system retrieved. | İçsel halüsinasyon |
| Extrinsic hallucination | A hallucination that the input can neither support nor contradict; it adds something from elsewhere. | Dışsal halüsinasyon |
| Recombination | Joining patterns learned from true text into a statement that is false. | Yeniden birleştirme |
| Sycophancy | Output that agrees with your stated view even when the evidence points the other way. | Dalkavukluk (yaranma eğilimi) |
| Prompt injection | Text that acts as an instruction to an AI system against its owner's intent; direct when a user types it, indirect when it is hidden in content the system retrieves. | İstem enjeksiyonu |
| Pushback test | A probe that challenges a correct answer to see whether the output changes to agree with you. | İtiraz testi |
| Failure-to-harm chain | The links by which an AI error becomes a harm: the output is wrong, it is not checked before use, someone relies on it, and a loss follows. | Hatadan zarara zincir |
| Failure Diary | A dated record of AI failures you met, each with the test that showed it, a label and likely causes. | Başarısızlık günlüğü |
| Confabulation (Deep) | Another word for hallucination, used by some researchers and by NIST's Generative AI Profile: confidently stated but false content. | Konfabulasyon (uydurma) |
| Task frame | A short statement of a task's goal, audience, success criteria, limits and what stays with you, written before the first prompt. | Görev çerçevesi |
| Success criteria | Checks, written in advance, that an output must pass to count as good; each can be scored met, partly met or not met. | Başarı ölçütleri |
| Delegation Ladder | The book's arrangement of three ways of working with AI over a floor of no AI, ordered by how hard it is to check what the AI contributed before it takes effect. | Devretme merdiveni |
| Automation (mode of working with AI) | Working with AI in which the AI carries out a task you define, and you check the output. | Otomasyon |
| Augmentation | Working with AI in which you and the AI shape and carry out the task together, turn by turn. | Güçlendirme (birlikte çalışma) |
| Agency (mode of working with AI) | Working with AI in which you configure it to carry out future tasks on your behalf, including for other people. Not the same as an agent. | Vekâlet kipi (ajanlık) |
| Anatomy of a prompt | The book's six-part description of what a prompt can contain: role, task, context, constraints, in-context examples and output format. | İstem anatomisi |
| Role (prompt part) | The voice or perspective the output takes; who will read the output belongs in the context. | Rol (istem bileşeni) |
| Task (prompt part) | What you want done: an action and what it acts on. The one part every prompt needs. | Görev (istem bileşeni) |
| Context (prompt part) | The background a task needs that the tool cannot otherwise receive, such as figures, readers or source text. | Bağlam (istem bileşeni) |
| Constraint | A limit or a must-not in a prompt, such as a length, a source rule or an excluded topic. | Kısıt |
| In-context example | A sample input with the output you want, placed in a prompt to show the pattern. | Bağlam içi örnek |
| Output format | The shape the output should take, such as a table, a list or a word limit, chosen so it can be checked. | Çıktı biçimi |
| Iteration | Improving a prompt by changing one thing at a time, predicting the effect, rerunning and scoring the result against your success criteria. | Yineleme |
| Iteration log | A record of each prompt version: what changed, the prediction, the results of each run and the decision to keep or revert. | Yineleme günlüğü |
| Test inputs | A small set of different inputs a prompt is tried on (typical, different, edge) to see whether it works beyond one case. | Test girdileri |
| Peer swap test | Someone else runs your prompt without your explanation and scores the output against your criteria, to reveal what was in your head but not in the prompt. | Akran takas testi |
| Benchmark | A standard test used to compare models. | Kıyaslama testi (benchmark) |
| Context layers | The separate sources of text that together fill a model's context window in one turn, each set by someone and at some time. | Bağlam katmanları |
| Context engineering | Deciding what goes into a model's context window, from which layer, in what form and in what order, so that a task can be done well. | Bağlam mühendisliği |
| Standing instructions | Instructions you write once, in a tool's options or a project, that the tool adds to every conversation in that scope. | Kalıcı talimatlar |
| Project space | A workspace in a tool where chosen files and instructions are added to every conversation started inside it. | Proje alanı |
| Gap instruction | A line in a prompt that says what to do when the material is not enough. | Boşluk talimatı |
| Prompt template | A prompt written for a recurring task, with fixed parts that stay the same each time and placeholders for the parts that change. | İstem şablonu |
| Placeholder | A marked slot in a template, such as {NOTES} or {DATE}, that you replace with new material each time you use it. | Yer tutucu |
| Prompt version | A numbered, dated state of a prompt or template, recorded with what changed and what it was tested on. | İstem sürümü |
| Prompt library | A personal or shared collection of tested prompt templates, each recorded with when to use it, what it was tested on and how it has changed. | İstem kütüphanesi |
| Prompt chain | A fixed sequence of prompts that you run one after another, where each step's output becomes the next step's input and you check the result between steps. | İstem zinciri |
| Claim | One statement in an output that you might rely on; marked checkable (it can be true or false) or not checkable as true or false (a judgment, recommendation or prediction). | İddia |
| Stakes (of a claim) | What would be lost, by you or by someone else, if the claim were wrong. | Risk (iddianın önemi) |
| Verification | Checking a claim against evidence that no AI tool produced. | Doğrulama |
| Verification Funnel | The book's diagram of three checks a claim can pass through (an independent check, the primary source, an expert), each outside the tool, taken only as far as the stakes require. | Doğrulama hunisi |
| Independent check | Evidence that no AI tool produced: a source with an author or publisher you can name, or your own recalculation or reasoning from known inputs. | Bağımsız kontrol |
| Primary source | The original record a claim comes from: the study, the dataset, the law, the court record, the official page of the organization that sets the rule. | Birincil kaynak |
| Verdict | A judgment on the book's five-point scale: supported (the evidence says what the claim says); partly supported (part holds, part does not or is missing); unsupported (no evidence for it at the stage you reached: nothing found, or the source does not say it); contradicted (the evidence says otherwise); cannot verify (the evidence exists or may exist, but you cannot reach it). | Hüküm (doğrulama sonucu) |
| Remaining uncertainty | What you could not check, and why; recorded with every verdict. | Kalan belirsizlik |
| Fabricated citation | A citation to a work that does not exist. | Uydurma kaynak gösterimi |
| Uncertainty signal | A feature of an output that makes an error more or less likely without settling whether a claim is true. | Belirsizlik işareti |
| Consistency check | Asking the same question in several new chats and comparing the answers. | Tutarlılık kontrolü |
| Stated confidence | The certainty an output expresses in words or numbers, such as "I'm 95% sure" or "definitely." | Beyan edilen güven |
| Calibration (of a model) | How closely a model's stated confidence matches its accuracy. | Kalibrasyon (modelin) |
| Calibration gap | Your predicted score minus your actual score, across a set of answers; divided by the number of questions, your average confidence minus the share you got right. A positive gap means you were overconfident. | Kalibrasyon farkı |
| Expected calibration error (Deep) | The average gap between confidence and accuracy across confidence groups, giving larger groups more weight. | Beklenen kalibrasyon hatası |
| Performance (during practice) | How well you do a task while practicing, often with help; it can differ from what you have learned. | Performans (alıştırma sırasında) |
| Learning (durable) | A lasting change in what you can do without help, shown later and in new situations. | Kalıcı öğrenme |
| Overreliance | Relying on an AI tool's output more than the task or the evidence warrants, so that your own checking or skill-building drops out. | Aşırı bağımlılık |
| Retrieval practice (learning) | Recalling information from your own memory, for example by self-testing, which strengthens it more than restudying. Not the same as retrieval in an AI system (Ch. 3). | Geri çağırma alıştırması |
| Desirable difficulty | A condition that makes learning feel harder and slower but improves long-term memory and use, provided you can meet it with effort. | İstenen zorluk |
| Generation effect (learning) | The finding that information you produce yourself is remembered better than information you only read. | Üretme etkisi |
| Spacing (spaced practice) | Spreading study of the same material over separate sessions instead of massing it in one. | Aralıklı çalışma |
| Metacognition | Knowing about and monitoring your own thinking and learning. | Üstbiliş |
| Calibration (of your own confidence) | How closely your confidence in your answers matches how often they are actually correct, across many answers. | Kalibrasyon (kendi güveninin) |
| Keyed questions | Questions that come with an answer key, such as a textbook's end-of-section or practice questions. | Cevap anahtarlı sorular |
| Scaffold | Temporary support that lets you do what you cannot yet do alone, withdrawn as you improve. | İskele (destek) |
| Crutch (in learning with AI) | Help that does the part of the work you needed to do yourself, and that you keep depending on. | Koltuk değneği |
| Tutor mode | A way of using an AI tool in which it is set up to respond with questions and hints and to wait for your attempts, instead of giving answers. | Öğretmen kipi |
| Answer mode | The default way of using an AI tool, in which it produces the answer or finished work you ask for. | Cevap kipi |
| Socratic questioning | Teaching by asking questions that lead the learner to reason the answer out. | Sokratik sorgulama |
| Cognitive offloading (Deep) | Using a tool or action to reduce the mental work a task requires, such as writing a note or using a calculator. | Bilişsel yük aktarımı |
| Secondary source | A source that reports on or interprets primary sources, such as a review article, a textbook or a news story about a study. | İkincil kaynak |
| Tertiary source | A source that collects and condenses secondary ones, such as an encyclopedia, an index or a study guide. | Üçüncül kaynak |
| Gray literature | Material published outside journals and books, such as reports by governments, companies, charities and consulting firms. | Gri literatür |
| Peer review | The checking of a research manuscript by a few experts in the field, at a journal editor's request, before publication. | Hakem değerlendirmesi |
| Preprint | A research manuscript posted publicly before peer review. | Ön baskı (hakem öncesi makale) |
| Correction (of an article) | A notice that fixes part of a published article. | Düzeltme |
| Retraction | The withdrawal of a published article because of serious error or misconduct. | Geri çekme |
| Abstract | The short summary at the start of a research article. | Özet (makale özeti) |
| Open access | Free to read online. | Açık erişim |
| Source ladder | The book's four-rung picture of how directly a source records a claim, judged from the source alone: 4, it is the record of this claim; 3, it cites the specific record or records a narrower part of the claim; 2, it names a source too vaguely to find; 1, it gives no source. | Kaynak merdiveni |
| Rung needed | The rung of the source ladder that your purpose and the stakes require for a claim. | Gereken basamak |
| Systematic review | A review that searches for every study on a question with a written plan. | Sistematik derleme |
| Vertical reading | Judging a page by its own look and its own claims. | Dikey okuma |
| Lateral reading | Leaving a page early to see what outside sources say about who is behind it. | Yanal okuma |
| Outside source | A source not written or paid for by whoever is behind the page you are checking. | Dış kaynak |
| Use decision | Your choice of how to use a source (rely on it, use it with a caveat, use it only as a lead, or do not use it); "rely on it" needs both a rung that meets your need and nothing in your outside sources that gives you reason to distrust who is behind it. | Kullanım kararı |
| Citation tracing | Following a claim from where you met it, hop by hop, to the place it first appeared, checking at each hop that the cited source says what the citing source claims. | Atıf izleme |
| Drift (in a retelling) | A change in a claim as it is retold: a dropped caveat, a broadened claim, a cause read into a correlation, or a changed number. | Kayma (aktarımda) |
| Correlation | Two things varying together, which does not show that one causes the other. | Korelasyon (birlikte değişim) |
| Summary fidelity | How closely a summary's claims match what the original supports. | Özet sadakati |
| Omitted key result | A finding that changes the picture but is missing from a summary. | Atlanmış temel bulgu |
| AI search | A tool that retrieves pages and then produces an answer with links (the search-then-generate lane). | Yapay zekâ destekli arama |
| Research-report tool | A system that runs many searches, retrieves many pages and produces a long report with citations; often marketed as "deep research." | Araştırma raporu aracı |
| Meta-analysis | A study that combines the results of many studies statistically into one estimate. | Meta-analiz |
| GRADE (Deep) | Grading of Recommendations Assessment, Development and Evaluation: a system that rates the certainty of a body of health evidence, starting from study design and moving the rating down or up. | GRADE (kanıt kesinliği derecelendirmesi) |
| Voice (in writing) | The impression of a writer that a reader forms from the writer's choices of words, sentence shapes, stance and what to include. | Yazar sesi |
| Ownership (of a text) | Having decided what a text says, and being able to explain, defend and stand behind every sentence in it and its consequences; not the same as legal authorship. | Metnin sahipliği |
| Voice and ownership spectrum | The book's five positions for a use of AI in writing, ordered by how much of the wording a tool supplies: your words only, AI as reader (you write every change), AI as editor (you accept or reject the tool's wording), AI as co-drafter, AI as author (sent as is). | Ses ve sahiplik yelpazesi |
| Ghostwriter | A person who writes a text that someone else signs. | Hayalet yazar |
| Write first | Putting down what you want to say, in notes or a rough draft, before you ask a tool for anything. | Önce yaz |
| Tone | The attitude a message conveys toward its reader and topic, such as formal, warm or brief. | Ton (üslup) |
| Homogenization | Becoming more alike; in writing, different writers' texts converging on the same phrasing. | Tekdüzeleşme |
| Stock phrase | A ready-made phrase used by many writers, such as "I am writing to inform you." | Kalıp ifade |
| Annotated draft | An AI-assisted draft with every sentence coded keep (K), rewrite (R) or reject (X) and tagged with a reason. | Açıklamalı taslak |
| Revision trace | A record of versions, from your notes or first draft to the tool's draft to your final version, with what changed, who or what proposed it, and why. | Revizyon izi |
| AI-text detector | A tool that gives a score for how likely a text is to have been generated by AI. | Yapay zekâ metin dedektörü |
| False positive (of a detector) | A human-written text labeled AI-generated; the false-positive rate is the share of human texts labeled that way. | Yanlış pozitif |
| Process evidence | The record of how you wrote: notes, earlier drafts, version history, revision trace, declaration, and your ability to explain your choices. | Süreç kanıtı |
| Disclosure (of AI use) | Telling the people who rely on a message how AI was involved in making it, in a form and place they will see. | Yapay zekâ kullanımının açıklanması |
| Perplexity (Deep) | Roughly, how unlikely a language model's scores make each next word; low perplexity means the words are easy to predict. | Şaşkınlık ölçüsü (perplexity) |
| Watermark (text; Deep) | A hidden statistical pattern in the tokens a provider's model favors, which a matching tool can later test for. | Filigran (dijital) |
| AI-mediated communication (Deep) | Communication between people in which software acts on behalf of one of them by changing, adding to or generating their message. | Yapay zekâ aracılı iletişim |
| Decision support | AI output, such as a summary, an analysis, a score or a recommendation, that goes to a named person who decides and answers for the result. | Karar desteği |
| Decision owner | The named person or body who makes a decision and answers for its result. | Karar sahibi |
| Automated decision | A decision in which an AI output triggers an action with no person in between. | Otomatik karar |
| Hidden assumption | A choice built into data or an analysis that can change the result but is not stated. | Örtük varsayım |
| Missing value | An empty cell or field where a value should be. | Eksik değer |
| Listwise deletion | Deleting every row that has a missing value, so the analysis uses complete rows only. | Liste boyunca silme |
| Imputation | Filling a missing value with an estimate, such as the average of the other values. | Eksik veri tamamlama (töhmet) |
| Proxy label | A recorded outcome used as the label because it is easy to measure, standing in for the outcome you actually care about. | Vekil etiket |
| Simpson's paradox | A pattern in a total that weakens or even reverses inside the groups that make it up. | Simpson paradoksu |
| Decision matrix | A table that lists options against the criteria they are judged on, each criterion with a scale and a weight. | Karar matrisi |
| Criterion (in a decision matrix) | One of the things the options are judged on, with its own scale. | Ölçüt |
| Weight (in a decision matrix) | How much a criterion counts toward the total. | Ağırlık |
| Sensitivity check | Changing one choice in an analysis, such as a weight or the handling of a blank, to see whether the result changes. | Duyarlılık kontrolü |
| Automation bias | The tendency to over-rely on automated output, following it when it is wrong or missing what it did not flag. | Otomasyon yanlılığı |
| Commission error | Following an automated output when it is wrong. | Yapma hatası |
| Omission error | Missing a problem because an automated system did not flag it. | İhmal hatası |
| Missing completely at random, MCAR (Deep) | Values are missing for a reason that has nothing to do with any data. | Tamamen rastgele eksiklik |
| Missing at random, MAR (Deep) | Values are missing for a reason that depends only on things you did observe. | Rastgele eksiklik |
| Missing not at random, MNAR (Deep) | Values are missing for a reason that depends on the missing value itself. | Rastgele olmayan eksiklik |
| Multiple imputation (Deep) | Filling each missing value several times with plausible values, analyzing each completed dataset and pooling the results with their extra uncertainty. | Çoklu tamamlama (çoklu töhmet) |
| Sensitivity analysis (Deep, missing data) | Assuming the missing values were somewhat higher or lower than the fill and checking whether the conclusion survives. | Duyarlılık analizi |
| Task–tool fit | How well one tool, used in one way, meets one task's success criteria within your limits of data and cost, on a given date. | Görev–araç uyumu |
| AI tool | The software you use: a model plus what the tool adds to the model's context window, what it can do, where the model runs and whose terms cover it. | Yapay zekâ aracı |
| Provider | The company or institution that runs an AI tool. | Sağlayıcı |
| Domain tool | A tool built for one field, often given that field's records or documents. | Alana özgü araç |
| Open-weight model | A model whose settings (parameters), called its weights, can be downloaded and run under a license. | Açık ağırlıklı model |
| Local model | An open-weight model run on hardware that you or your institution control, so your input need not go to the model's provider. | Yerel model |
| Total cost of use | The price of a tool, plus usage limits, the time spent checking outputs, the time spent learning the tool, what you give up in data, and the cost of switching later. | Toplam kullanım maliyeti |
| Verification cost | The time and effort needed to confirm that an output meets your criteria. | Doğrulama maliyeti |
| No-AI baseline | The time a part of a task takes you without any AI tool, done well enough to meet your criteria. | Yapay zekâsız başlangıç ölçüsü |
| Data terms | The parts of a tool's terms and its options that say what happens to what you type and upload. | Veri koşulları |
| Data class | The category an institution assigns to information by how much harm its release could cause; UTD's policy names three: Public Data, Controlled Data and Confidential Data. | Veri sınıfı |
| Data gate | A check, made before any quality test, of whether a tool's data terms fit the class of the input. | Veri kapısı |
| Bake-off | A side-by-side test of two or more tools, and where possible no AI, on the same part of a task. | Karşılaştırmalı deneme (bake-off) |
| Fit matrix | A table whose rows are the parts of a task and whose columns are the tools you tested plus no AI; each cell holds a fit decision, its rung and its reason. | Uyum matrisi |
| Drift (in a tool or model over time) | A change in how a named model or tool behaves on the same inputs over time, often after its provider updates it. | Kayma (araç ya da modelde zamanla) |
| Lock-in | The effort and cost that keep you on a tool after a better fit appears. | Bağımlılık (kilitlenme) |
| Re-test trigger | An event that should make you test a fit again, such as a model update or retirement, a change in price or terms, a new kind of input, or a change of job or school. | Yeniden test tetikleyicisi |
| Leaderboard (Deep) | A ranking of models by benchmarks or by crowd votes. | Sıralama tablosu (leaderboard) |
| Modality | A kind of data, such as text, images, audio or video. | Kip (veri türü) |
| Multimodal model | A model that receives or produces more than one kind of data, such as text, images, audio or video. | Çok kipli model |
| Image token | A small square patch of an image, turned into numbers that a multimodal model receives the way it receives text tokens. | Görüntü belirteci |
| Audio token | A short slice of sound compressed into a code that a model can receive or produce like a text token. | Ses belirteci |
| Diffusion model | A generator that starts from random noise and removes it step by step, guided by a prompt, until an image (or audio or video) appears. | Difüzyon modeli |
| Synthetic media | Images, audio or video generated or substantially altered by AI. | Sentetik medya |
| Deepfake | Synthetic media that realistically shows a real person, or a real event, saying, doing or happening in a way that did not happen. | Derin sahte (deepfake) |
| Voice cloning | Using AI to produce new speech that imitates a particular person's voice from samples of it. | Ses klonlama |
| Alt text | A short text alternative for an image that tells a reader who cannot see it what they need to know from it. | Alternatif metin |
| Closed captions | On-screen text of a video's speech and important sounds, which viewers can turn on or off. | Kapalı altyazı |
| Transcription (speech recognition) | Turning spoken audio into written text. | Döküm (konuşma tanıma) |
| Provenance | A record of where a piece of content came from and how it was changed. | Köken kaydı (provenans) |
| Metadata | Data about a file, such as when, where and with what it was made. | Üst veri |
| Content credentials | A provenance record attached to a file under the C2PA standard: signed statements about how the file was made and edited. | İçerik kimlik bilgileri |
| Watermark (media) | A pattern, visible or hidden, that a tool places in the image, audio or video it produces, which a matching detector can later test for. | Filigran (medya) |
| Deepfake detector | A tool that gives a score for how likely an image, audio or video is to have been generated or altered by AI. | Derin sahte dedektörü |
| Reverse image search | Searching with an image, instead of words, to find where it or similar images appear online, including its earliest version. | Tersine görsel arama |
| Out-of-band check | Confirming a request or a claim through a separate channel you already trust, not one the message provides. | Kanal dışı doğrulama |
| Social engineering | Manipulating people, rather than breaking into systems, to get them to give money, access or information. | Sosyal mühendislik |
| Cheap fake | Media manipulated without generative AI, such as a real photo with a false caption or date, a slowed-down video or a simple edit (Paris & Donovan, 2019). | Ucuz sahte (cheap fake) |
| Liar's dividend | The benefit a person gains by dismissing real recordings as fake when fakes are common (Chesney & Citron, 2019). | Yalancının kazancı |
| Verification protocol | Rules you write in advance for when and how you check media and media-borne requests before you act on them. | Doğrulama protokolü |
| Workflow | A fixed sequence of steps for a task, run by people, by software or by both. | İş akışı |
| Automated workflow | A workflow whose steps software runs, along a path people fixed in advance. | Otomatik iş akışı |
| Agent loop | The cycle an agent repeats: the model produces a plan for the next action, the system runs the tool call, and the result, the observation, is added to the context window, until a stop condition is met. | Ajan döngüsü |
| Error compounding | The tendency for the chance of an error-free run to fall as steps are added, because each step is another chance for an error and later steps can build on earlier ones. | Hata birikmesi |
| Reversible action | An action whose effect can be undone at little cost, such as a draft, an item in a cart or a change in a test copy. | Geri alınabilir eylem |
| Approval gate | A point at which a system pauses before an action takes effect until a named person approves, edits or rejects it. | Onay kapısı |
| Check point | A point at which a person inspects an intermediate result before later steps build on it (not a saved restore point). | Kontrol noktası |
| Stop point | A condition at which a run halts and hands control back to a person, such as a step, time or spending limit, an error, or an unexpected result. | Durma noktası |
| Soft gate | An instruction in the context asking the model to ask first or not to act; the model receives it as text and may not follow it. | Yumuşak kapı |
| Hard gate | A gate the system enforces outside the model, so the action cannot run unless a person acts, or cannot run at all. | Sert kapı |
| Approval fatigue | Approvals given so often or so quickly that they stop working as checks. | Onay yorgunluğu |
| Least privilege | Giving each tool and account only the access its step needs, for only as long as it is needed. | En az yetki |
| Sandbox | A separate test copy where changes do not reach real data or people. | Korumalı alan (test ortamı) |
| Log (of an agent run) | A record the system writes as it runs of every plan, tool call, observation, approval and stop, with times. | Kayıt (ajan çalışma günlüğü) |
| Dry run | Running a whole workflow on test inputs with real effects switched off, before anyone relies on it. | Kuru çalıştırma (prova) |
| Planted fault | An error put into one step of a dry run on purpose, to see whether a check point, gate or stop point catches it. | Yerleştirilmiş hata |
| Done-criteria | Two or three checks that tell you whether a run succeeded. | Tamamlanma ölçütleri |
| Workflow blueprint | A written design of a workflow: its steps, who or what runs each, its actions, people points, permissions, log plan and dry-run results. | İş akışı planı |
| Data-flow map | A drawing of where one input goes once you send it: what goes in, where it is stored, who can see it, whether it is reused and where the output goes. | Veri akış haritası |
| Trust boundary | The line past which your data is handled under someone else's rules. | Güven sınırı |
| Personal data | Information about an identified or identifiable person (also called personally identifiable information, PII). | Kişisel veri |
| Sensitive data | Personal data that can do special harm if exposed, such as biometric, health or location data. | Hassas veri |
| Biometric data | Data about a person's body or behavior, such as a face, a voice, a fingerprint or the way someone walks. | Biyometrik veri |
| Quasi-identifier | A detail that is harmless alone but identifying together with others, such as ZIP code, sex and date of birth. | Yarı tanımlayıcı |
| Re-identification | Linking quasi-identifiers with another record, such as a voter list, to learn who a person in a dataset is. | Yeniden kimliklendirme |
| De-identification | Removing names and obvious identifiers from data; a start, not a guarantee that the data is anonymous. | Kimliksizleştirme |
| Data minimization | Sending only what a part of a task needs. | Veri en aza indirme |
| Inference (of personal attributes) | A model producing a likely personal detail that a text never states, such as a writer's location; not the same as Chapter 3's inference, running a model. | Çıkarım (kişisel özelliklere dair) |
| Exfiltration | Getting data out of a system to an attacker. | Veri sızdırma (dışarı çıkarma) |
| Defense in depth | Several layers of defense, built to fail in different ways. | Katmanlı savunma |
| Lethal trifecta | Willison's (2025) name for a system that combines three legs, access to private data, exposure to untrusted content and a way to send data out, which together allow data theft. | Ölümcül üçlü |
| Dual authorization | A control under which two people must approve a payment or an account change. | Çift onay |
| Risk | A combination of how likely a harmful event is and how bad its consequences would be (after NIST, 2023). | Risk |
| Likelihood (of a risk) | How probable a harmful event is, rated low, medium or high by written anchors. | Olasılık (riskin) |
| Impact (of a risk) | How bad the consequences of a harmful event would be, rated low, medium or high by written anchors. | Etki (riskin) |
| Risk Heat Map | Signature 10: a 3-by-3 grid of likelihood by impact on which each risk is placed, with its evidence marked documented or inferred; risks in the high-impact row need a mitigation or a named owner. | Risk ısı haritası |
| Risk register | A list of risks with their ratings and evidence. | Risk kaydı |
| Mitigation | A change that lowers a risk's likelihood, its impact or both; this book uses four kinds: avoid, reduce, detect, accept. | Risk azaltma (önlem) |
| Residual risk | The risk that remains after mitigation. | Kalıntı risk |
| Qualifying risk | A risk that needs a full mitigation plan in A12: its impact is high, or both its likelihood and its impact are at least medium. | Plan gerektiren risk |
| Risk owner | The person who agrees in writing to carry a risk. | Risk sahibi |
| Red-teaming | Testing a system the way an attacker would, with permission, to find weaknesses first. | Kırmızı takım testi |
| Bias (in an AI system) | A systematic difference in how a system's outputs or errors fall on different groups of people that disadvantages some of them. | (Yapay zekâ sisteminde) yanlılık |
| Bias Lifecycle | The book's four-phase picture of where bias can enter an AI system: data, model, use and feedback. | Yanlılık yaşam döngüsü |
| Allocation harm | Harm that withholds an opportunity or resource, such as a job or a place in a program. | Dağıtım zararı |
| Representation harm | Harm that stereotypes, demeans or leaves out a group in what people see and read. | Temsil zararı |
| Feedback loop (in an AI system) | A path by which a system's decisions become its next data, so a gap between groups can grow. | Geri besleme döngüsü |
| Disaggregated evaluation | Reporting a system's performance separately for each group and subgroup instead of one overall number. | Ayrıştırılmış değerlendirme |
| Intersectional subgroup | A group defined by two or more characteristics at once, such as darker-skinned women. | Kesişimsel alt grup |
| Fairness definition | A stated rule for which comparison between groups must come out equal. | Adalet tanımı |
| Selection rate | The share of a group that a tool flags. | Seçilme oranı |
| Base rate | How often the outcome actually occurs in a group. | Temel oran |
| Equal selection rates | A fairness definition: the same share of each group is flagged (demographic parity). | Eşit seçilme oranları |
| Equal error rates | A fairness definition: the same share missed, and the same share flagged wrongly, in each group. | Eşit hata oranları |
| Equal precision | A fairness definition: a flag means the same in each group; of the flagged, the same share were really positive (predictive parity). | Eşit kesinlik |
| Miss rate | The share of real cases not flagged (one minus recall). | Kaçırma oranı |
| False-positive rate (of a decision tool) | The share of people without the outcome who are flagged anyway. | (Karar aracının) yanlış pozitif oranı |
| Paired-input test | A test that runs inputs identical except for one cue linked to a group, many times each, counts the outputs by a rule fixed before any run, and compares the counts. | Eşleştirilmiş girdi testi |
| Two-part rule | A gap is a finding only if (1) the test was fair (one change, a fixed counting rule, one tool, fresh chats, the same number of runs per version, at least 10) and (2) the gap is at least the chance threshold; otherwise it is a lead. | İki koşullu kural |
| Chance threshold | The smallest gap, in either direction, that chance alone reaches less than 1 time in 20 when both versions truly give the pattern 50% of the time. | Şans eşiği |
| Bias probe | A paired-input test used as A12's red-team probe. | Yanlılık yoklaması |
| Mitigation (of bias) | A change meant to reduce a measured bias. | (Yanlılığı) azaltma önlemi |
| Protected characteristic | A characteristic, such as race or sex, that anti-discrimination law says decisions such as hiring must not be based on. | Korunan özellik |
| Stakeholder | Everyone affected by a decision, including people who never use the tool. | Paydaş |
| Bias audit | A structured test of whether a system's outputs or errors differ across groups, recorded with its method, counts and decisions. | Yanlılık denetimi |
| Calibration within groups (Deep) | A score means the same chance of the outcome in every group (a score of 0.7 means a 70% chance). | Gruplar içi kalibrasyon |
| Runaway feedback loop (Deep) | A feedback loop in which a system keeps being sent back to where it already looked, whatever the true rate. | Kontrolden çıkan geri besleme döngüsü |
| Predictive policing (Deep) | Software that sends patrols to areas where past records show more crime. | Öngörücü polislik |
| Explainability | How far people can get reasons for a system's outputs that they can understand and use. | Açıklanabilirlik |
| Appropriate reliance | Relying on a system when it is right and not relying on it when it is wrong (after Lee & See, 2004). | Uygun güven (yerinde dayanma) |
| Transparency (of an AI system) | Openness about a system: whether it is used, what it is for, what data and logic it relies on, how it was tested and who answers for it. | Şeffaflık (yapay zekâ sisteminin) |
| Interpretability | How far a person can follow how a model turns inputs into outputs from the model itself. | Yorumlanabilirlik |
| Black box | A system whose inputs and outputs can be seen but whose internal workings are not visible, or not understandable, to the people who use it or are affected by it. | Kara kutu |
| Interpretable model | A model whose decision process a person can follow from the model itself, such as a points scorecard, a short list of rules or a small decision tree; sometimes called a glass box. | Yorumlanabilir model (cam kutu) |
| Post-hoc explanation | An explanation produced after a model is built, by a separate method that studies the model's inputs and outputs. | Sonradan (post-hoc) açıklama |
| Global explanation | An explanation of how a model behaves across many cases, such as which features matter most overall. | Genel (küresel) açıklama |
| Local explanation | An explanation of why a model produced one output for one case. | Yerel açıklama |
| Feature attribution | An explanation that assigns each input feature a share of the credit for an output, for one case or across many. | Özellik atfı |
| Counterfactual explanation | An explanation that names the smallest change to an input that would have changed the output. | Karşı-olgusal açıklama |
| Recourse | A counterfactual change that a person can actually make. | Telafi yolu (başvuru imkânı) |
| Example-based explanation | An explanation that shows past cases a model treated as similar, or typical examples of each outcome. | Örnek tabanlı açıklama |
| Faithfulness (of an explanation) | How accurately an explanation reflects the process that actually produced the output. | Sadakat (açıklamanın) |
| Surrogate model | A simpler model trained to imitate a complex one, often to explain it. | Vekil model |
| Fidelity (of a surrogate model) | How often a surrogate model gives the same output as the model it imitates. | Uygunluk oranı (vekil modelin) |
| Chain-of-thought text | The step-by-step text a model produces before or with its answer, sometimes shown and sometimes hidden as reasoning tokens. | Düşünce zinciri metni |
| Model card | A short document published with a model that states what it is for and not for, how it was evaluated, including results by group where relevant, and its known limits (after Mitchell et al., 2019). | Model kartı |
| System card | A provider's document about a released AI system, describing its evaluations, known risks and safety measures. | Sistem kartı |
| Algorithm register | A public list of the algorithms an organization uses, with their purpose and a contact. | Algoritma sicili |
| Right to contest | Being able to challenge a decision before a person who can review and change it. | İtiraz hakkı |
| Personal AI code of practice | A short set of commitments you choose for how you will use AI in your own work, each written so that you recognize when it applies, with a date to review it. | Kişisel yapay zekâ uygulama ilkeleri |
| Professional code of ethics | A statement of principles a profession sets for its members. | Meslek etiği kodu |
| Commitment (in a code of practice) | A line in your code that states an action you will take. | Taahhüt |
| Trigger (in a code of practice) | The observable situation that tells you a commitment applies now. | Tetikleyici (uygulama ilkelerinde) |
| Own evidence (in a code of practice) | Something from your own work that shows why a line matters to you, such as a Failure Diary entry, an assignment result or a lab record; a rule counts only together with it. | Kendi kanıtın |
| Trigger test | Three questions a line must pass: would you notice the moment at the time, could you or someone else trace afterward that you acted, and does the reason point to your own evidence? | Tetikleyici testi |
| Review date | The date by which you reread your whole code and keep, revise or retire each line. | Gözden geçirme tarihi |
| Dated note | A fact about a tool or a rule, written with the date it was true: "as of [month year]." | Tarihli not |
| Implementation intention (Deep) | A plan that links a goal you already hold to a cue in the world, in the form "if this situation arises, I will respond this way." | Uygulama niyeti |
| Ethics washing (gloss, Ethics Lens) | A statement of good principles that makes a person or company look responsible without changing what they do. | Etik aklama |
