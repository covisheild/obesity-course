# Obesity Expertise · The Subject Map

**A staged competency curriculum derived from *Obesity Expertise: A First-Principles Curriculum*. 61 subjects across 18 parts, each broken into an unbroken ladder of levels from Introductory upward, with the concepts, skills, build target and completion gate for every rung.**

**Version 3.** Version 1 and 2 assigned each subject a single target level and listed its requirements as one flat set. This version replaces that flat set with a staircase: every bullet has been re-sorted into the rung at which it is first needed, so the requirement now tells you not only what the subject demands but in what order to acquire it.

---

## How this document works

Each of the 61 subjects carries a **target level** — the depth the source document's goal actually requires. Underneath it sits a **ladder** running from Introductory up to that target. There are **195 rungs in total**: 61 Introductory, 60 Intermediate, 55 Advanced and 19 Expert.

Every rung has four parts:

- **Concepts to understand** — the ideas that rung requires, and only those. A concept appears at the rung where it is first needed and is then assumed by every rung above it.
- **Skills to demonstrate** — actions, written so someone else could watch you do them and judge. Not topics.
- **Build target** — the thing you make at that rung. A rung is not finished when you understand it; it is finished when the artefact exists. This follows the source document's own discipline: every block of study should be producing a specific analysis, a teaching session or a draft, never just understanding.
- **Gate to the next rung** — one observable pass/fail test. If you cannot honestly claim the gate, you are still on that rung.

**The completion rule.** Rungs are ordered and you finish one before starting the next, including its build target. This is not a suggestion about study habits; the ladders are written so that the concepts at each rung presuppose the rung below. Skipping a rung leaves a gap that shows up later as a result you cannot defend.

**The chain requirement.** Within a subject, the ladder is continuous: no rung introduces a concept whose prerequisite has not already appeared, and no rung repeats what the rung below already established. Across subjects, the prerequisite column in the register does the same job.

---

## The four levels

The rubric is absolute and behavioural. A level is what you can independently **do**, never what you have read.

| Level | Short form | The standard | The test |
| --- | --- | --- | --- |
| **Introductory** | Recognise and route | You know the vocabulary, know what the subject can and cannot answer, and know which specialist to call. You execute nothing in it. | Can you name the right specialist and formulate the right question? |
| **Intermediate** | Read, critique and commission | You can tell a good paper from a bad one, specify what you need from a specialist, supervise the work and judge the output. You may not be able to run it unaided. | Could you referee it, and could you reject a bad proposal with reasons? |
| **Advanced** | Execute and defend | You can do it yourself, end to end, on your own problem, and defend every choice to a specialist reviewer. This is the working standard for anything you will publish, prescribe or implement. | Could you run it alone and survive a hostile reviewer? |
| **Expert** | Originate and adjudicate | You can derive it from first principles and teach it without notes, extend or adapt the method, settle a dispute between two competent people, and publish work that changes how others do theirs. | Could you examine someone else in it, and would your judgement be accepted? |

**Ladders stop at the target.** A subject capped at Intermediate has two rungs and no more. That is deliberate: machine learning, agent-based modelling, comparative policy, health financing, Python and the adjacent specialist domains are places where going deeper is available, interesting and wrong — they return less per hour than the subject next to them, and they are the most plausible route to ten years of interesting study with nothing built. The cap is as load-bearing as the spike.

**Where the spikes are.** 19 subjects carry an Expert target, and they cluster rather than scatter: measurement, causal inference, nutritional epidemiology, the Indian phenotype, circadian biology, Indian data and Indian regulation. Nineteen Expert targets is the shape of a completed career, not a plan for one year. If you are choosing where to buy depth first, the map's own internally consistent answer is **S08 measurement error, S11 causal diagrams and structural bias, S33 circadian biology and chrononutrition, S54 India's data infrastructure** — each under-occupied in India, each compounding into the others.

**Where to start today.** Eleven subjects have no prerequisites inside this map, and their Introductory rungs can be started this week: S01, S02, S36, S37, S47, S52, S55, S57, S58, S59 and S61. Of these, S52 rung 1 (one dataset analysed end to end in a runnable script) and S55 rung 1 (ten candidate questions scored against the who-is-waiting test) have the highest downstream leverage, because everything else in the map eventually passes through them.

---

## Coverage audit

Every one of the 58 items in the source document's own competency checklist maps to at least one subject, and so does every step of its twelve-step causal spine. Ten subjects are *not* reachable from the checklist — S04, S06, S07, S12, S17, S23, S36, S43, S49 and S61. These come from the layer prose, which treats them as Core or Working without giving them a checklist line. That is a gap in the checklist rather than in the curriculum.

The 602 requirement bullets from version 2 have all been re-sorted into rungs; none were dropped, and several were split where one bullet spanned two levels.

---

## Subject register

Target level, number of rungs, prerequisites and study tier. **Tier** is a topological ordering: everything in tier 1 has no prerequisites inside this map, tier 2 depends only on tier 1, and so on. It is a dependency ordering, not a schedule.

| # | Subject | Part | Target | Rungs | Prerequisites | Tier |
| --- | --- | --- | --- | --- | --- | --- |
| S01 | Energy balance and dynamic weight-change modelling | Physical and mathematical foundations | **Expert** | 4 | — | 1 |
| S02 | Mathematics for modelling and inference | Physical and mathematical foundations | **Advanced** | 3 | — | 1 |
| S03 | Probability and statistical inference | Statistical inference and modelling | **Expert** | 4 | S02 | 2 |
| S04 | Regression modelling for health outcomes | Statistical inference and modelling | **Expert** | 4 | S03 | 3 |
| S05 | Clustered, longitudinal, hierarchical and small-area models | Statistical inference and modelling | **Advanced** | 3 | S04 | 4 |
| S06 | Evidence synthesis and meta-analysis | Statistical inference and modelling | **Advanced** | 3 | S04 | 4 |
| S07 | Prediction modelling and machine learning | Statistical inference and modelling | **Intermediate** | 2 | S04 | 4 |
| S08 | Measurement error theory and correction | Measurement science | **Expert** | 4 | S03, S04 | 4 |
| S09 | Measurement instruments: body composition, expenditure, diet, activity, sleep | Measurement science | **Expert** | 4 | S01, S08 | 5 |
| S10 | Potential outcomes, identification and target trial emulation | Causal inference | **Expert** | 4 | S03 | 3 |
| S11 | Causal diagrams, structural bias and sensitivity analysis | Causal inference | **Expert** | 4 | S10 | 4 |
| S12 | G-methods, time-varying treatment and mediation | Causal inference | **Advanced** | 3 | S10, S11, S04 | 5 |
| S13 | Instrumental variables and Mendelian randomisation | Causal inference | **Advanced** | 3 | S10, S11 | 5 |
| S14 | Quasi-experimental policy evaluation | Causal inference | **Advanced** | 3 | S10, S11, S05 | 5 |
| S15 | Study and trial design, power and missing data | Epidemiology | **Advanced** | 3 | S03, S10 | 4 |
| S16 | Genetics, developmental origins and life-course epidemiology | Epidemiology | **Expert** | 4 | S10, S15 | 5 |
| S17 | Social epidemiology, equity measurement and surveillance in India | Epidemiology | **Advanced** | 3 | S15 | 5 |
| S18 | Nutritional epidemiology and its pathologies | Epidemiology | **Expert** | 4 | S08, S10, S11, S15 | 5 |
| S19 | Integrative metabolism, insulin resistance and energy expenditure regulation | Metabolic and appetite biology | **Advanced** | 3 | S01 | 2 |
| S20 | Adipose tissue biology, ectopic fat and the South Asian phenotype | Metabolic and appetite biology | **Expert** | 4 | S19 | 3 |
| S21 | Appetite, reward and the determinants of intake | Metabolic and appetite biology | **Expert** | 4 | S19 | 3 |
| S22 | Clinical assessment, staging and secondary causes | Clinical obesity medicine | **Advanced** | 3 | S19, S20 | 4 |
| S23 | Lifestyle, dietary and behavioural treatment | Clinical obesity medicine | **Advanced** | 3 | S22, S27 | 5 |
| S24 | Pharmacotherapy of obesity | Clinical obesity medicine | **Advanced** | 3 | S21, S22 | 5 |
| S25 | Metabolic and bariatric surgery: selection and co-management | Clinical obesity medicine | **Advanced** | 3 | S22 | 5 |
| S26 | Life-stage obesity: paediatric, adolescent and pregnancy | Clinical obesity medicine | **Advanced** | 3 | S16, S22 | 6 |
| S27 | Nutrient science for obesity and cardiometabolic risk | Nutrition science | **Advanced** | 3 | S19 | 3 |
| S28 | Ultra-processed food and the effects of processing | Nutrition science | **Advanced** | 3 | S18, S21, S27 | 6 |
| S29 | Indian dietary patterns, guidelines, food composition and diet cost | Nutrition science | **Advanced** | 3 | S27 | 4 |
| S30 | Physical activity and sedentary behaviour science | Movement, sleep and circadian biology | **Advanced** | 3 | S19 | 3 |
| S31 | Activity measurement and compositional 24-hour analysis | Movement, sleep and circadian biology | **Expert** | 4 | S09, S30, S02 | 6 |
| S32 | Sleep science and obstructive sleep apnoea | Movement, sleep and circadian biology | **Advanced** | 3 | S19 | 3 |
| S33 | Circadian biology and chrononutrition | Movement, sleep and circadian biology | **Expert** | 4 | S19, S21, S32 | 4 |
| S34 | Behavioural theory, choice architecture and intervention design | Behavioural and psychological science | **Advanced** | 3 | S21 | 4 |
| S35 | Eating behaviour, mental health and weight stigma | Behavioural and psychological science | **Expert** | 4 | S21, S22 | 5 |
| S36 | Qualitative and mixed methods | Behavioural and psychological science | **Advanced** | 3 | — | 1 |
| S37 | Food systems, value chains and Indian food policy | Food systems and commercial determinants | **Advanced** | 3 | — | 1 |
| S38 | Food environment measurement, retail and digital delivery | Food systems and commercial determinants | **Advanced** | 3 | S15, S37 | 5 |
| S39 | Commercial determinants and corporate political activity | Food systems and commercial determinants | **Advanced** | 3 | S37 | 2 |
| S40 | Food demand, elasticity and the economics of externality | Economics and decision modelling | **Advanced** | 3 | S04, S29 | 5 |
| S41 | Fiscal instruments: taxation and subsidy design in India | Economics and decision modelling | **Advanced** | 3 | S40, S37 | 6 |
| S42 | Burden of disease, economic evaluation and decision-analytic modelling | Economics and decision modelling | **Advanced** | 3 | S02, S05, S40 | 6 |
| S43 | Health financing, HTA and pharmaceutical access in India | Economics and decision modelling | **Intermediate** | 2 | S42, S24 | 7 |
| S44 | System dynamics and complexity concepts | Systems and complexity | **Advanced** | 3 | S02 | 2 |
| S45 | Participatory systems mapping and group model building | Systems and complexity | **Advanced** | 3 | S44, S36 | 3 |
| S46 | Agent-based and network modelling | Systems and complexity | **Intermediate** | 2 | S44 | 3 |
| S47 | Policy process, framing and advocacy craft | Policy, law and political economy | **Advanced** | 3 | — | 1 |
| S48 | Indian regulatory architecture and the live policy agenda | Policy, law and political economy | **Expert** | 4 | S47, S37 | 2 |
| S49 | Comparative and international policy | Policy, law and political economy | **Intermediate** | 2 | S47 | 2 |
| S50 | Implementation science and programme craft | Implementation and health systems delivery | **Advanced** | 3 | S15, S36 | 5 |
| S51 | The Indian health system and its financing mechanics | Implementation and health systems delivery | **Advanced** | 3 | S50 | 6 |
| S52 | R, reproducibility engineering and data management | Computation and data | **Expert** | 4 | — | 1 |
| S53 | Python for simulation, scraping and tooling | Computation and data | **Intermediate** | 2 | S52 | 2 |
| S54 | India's data infrastructure, access and complex survey analysis | Computation and data | **Expert** | 4 | S52, S17 | 6 |
| S55 | Question selection and research strategy | Research craft | **Expert** | 4 | — | 1 |
| S56 | Protocol, preregistration, reporting standards and research ethics | Research craft | **Advanced** | 3 | S55, S15 | 5 |
| S57 | Teaching, mentorship and coalition building | Teaching, communication and integrity | **Advanced** | 3 | — | 1 |
| S58 | Scientific writing, visualisation and public communication | Teaching, communication and integrity | **Advanced** | 3 | — | 1 |
| S59 | Epistemics: philosophy of science and calibration | Teaching, communication and integrity | **Advanced** | 3 | — | 1 |
| S60 | Ethics of obesity intervention and industry engagement | Teaching, communication and integrity | **Expert** | 4 | S35, S39 | 6 |
| S61 | Adjacent specialist domains: recognise and route | Teaching, communication and integrity | **Introductory** | 1 | — | 1 |

---

# Part 1 · Physical and mathematical foundations

## S01 · Energy balance and dynamic weight-change modelling

**Target level: Expert** — originate and adjudicate · *Prerequisites: none* · *Part 1 · Physical and mathematical foundations* · *Source: Layer 1 Physics; spine steps 1–2*

**Why this level.** This is the one subject in the whole map where you cannot afford to be a consumer. It is the opening of every lecture you will give, the filter that lets you discard whole classes of claim without argument, and the place where a single wrong sentence in public costs you credibility with physiologists permanently. It is also cheap: the content is small, it is stable, and it does not decay.

**What it buys you in real life.** Immunity to the two commonest failures in this field — the crank claim that thermodynamics does not apply, and the naive claim that because thermodynamics applies, eating less is sufficient. You will use it weekly in teaching and in peer review, and it is the cheapest available demonstration of technical seriousness in a room of clinicians.

**The ladder — 4 rungs.** Complete each rung, including its build target, before starting the next.

### S01 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- Body fat is stored chemical energy and energy is conserved, so fat mass changes if and only if intake differs from expenditure.
- The units: kcal and kJ, and the order of magnitude of a day of intake, a day of expenditure and a kilogram of fat.
- Intake and expenditure are outputs of a regulated system, not dials you set — restrict intake and expenditure falls.

**Skills to demonstrate**

- State the first law as it applies to the body, in one sentence, without implying it names a lever.
- Spot a claim that violates conservation of energy and say so.

**Build target.** A one-page written explanation of why energy balance is arithmetically true and practically insufficient, tested on a non-medical reader.

**Gate to the next rung.** You can explain the accounting identity in three minutes without presenting it as a mechanism or a moral argument.

### S01 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- Energy densities of fat and lean tissue (roughly 39.5 and 7.6 MJ/kg) and why the difference matters for interpreting a weight change.
- Why the static 3500 kcal per pound rule is wrong: a deficit changes body mass, which changes maintenance requirement.
- Weight approaching a new asymptote rather than declining linearly, stated qualitatively.
- Gross combustion energy versus digestible versus metabolisable energy; Atwater factors as empirical approximations that fail for whole nuts, resistant starch and high-fibre foods.

**Skills to demonstrate**

- Critique a published weight-loss projection that assumes linear decline.
- Read Hall's dynamic energy balance papers and follow the argument without the mathematics.

**Build target.** An annotated teardown of one popular weight-loss claim, identifying which step breaks and why.

**Gate to the next rung.** You can explain why weight loss plateaus without invoking willpower failure or damaged metabolism.

### S01 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- The balance equation as a first-order ODE in fat and lean mass, with expenditure written as a function of state.
- Derivation of the time constant — roughly a year for most of the effect in adults — and what sets it.
- Energy partitioning between fat and lean, and the Forbes relationship, known by heart.
- How protein intake, training stimulus and baseline composition move the partition.

**Skills to demonstrate**

- Write, solve and plot the linearised energy-balance ODE and extract the time constant.
- Compute whether a reported weight change is thermodynamically consistent with a reported intake change.
- Estimate the magnitude of misreporting implied by the gap, which is almost always the explanation.

**Build target.** Reproduce one published intervention's weight trajectory in a solver (or Hall's body weight simulator) and compare it against the reported trajectory.

**Gate to the next rung.** Given a trial abstract, you produce the consistency check with numbers in under ten minutes.

### S01 · Rung 4 — Expert (originate and adjudicate)

**Concepts to understand**

- The two-compartment formulation with expenditure as an explicit function of both state and intake — the entire conceptual content of the equation.
- Non-equilibrium thermodynamics: the first law constrains the accounting, the second permits different metabolic efficiencies between substrate routes, and the empirical size of that difference is small relative to appetite effects.
- Biomechanics of locomotion: cost of transport, why walking is metabolically cheap per kilometre, and why exercise prescriptions built on expenditure alone underdeliver.

**Skills to demonstrate**

- Derive the equation from memory on a whiteboard and teach it to a first-year resident in twenty minutes.
- Adjudicate a dispute between an energy-balance advocate and a carbohydrate-insulin advocate by stating precisely what each side is and is not entitled to claim.
- Referee a submitted paper on dietary intervention for thermodynamic coherence.

**Build target.** A taught module on energy balance, plus one published commentary or correspondence correcting a thermodynamically inconsistent claim in the literature.

**Gate to the next rung.** A resident you taught reproduces the derivation unaided a week later.

---

## S02 · Mathematics for modelling and inference

**Target level: Advanced** — execute and defend · *Prerequisites: none* · *Part 1 · Physical and mathematical foundations* · *Source: Layer 1 Mathematics*

**Why this level.** You need to build and debug models, not prove theorems. Advanced means you can set up a system and solve it correctly; it does not mean measure-theoretic probability or real analysis, which pay essentially nothing here and are the most seductive time sink available to a first-principles thinker with a medical degree.

**What it buys you in real life.** Almost nobody in Indian public health can turn a verbal causal story into a solvable dynamic system. That single capability is the entry ticket to the systems and economics layers, and without it those layers degrade into diagram-drawing.

**The ladder — 3 rungs.** Complete each rung, including its build target, before starting the next.

### S02 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- Derivatives as rates and integrals as accumulation, applied to body stores rather than to abstract functions.
- What a matrix is and what multiplying by one does; vectors as data rows.
- Random variable, expectation and variance as mathematical objects distinct from their statistical use.
- What an equilibrium of a dynamic system is.

**Skills to demonstrate**

- Read an equation in a methods section and say what each symbol denotes.
- Follow a derivation in a paper without skipping to the result.

**Build target.** A worked notebook of ten equations taken from papers you have read, each annotated in words.

**Gate to the next rung.** You no longer skip equations when reading.

### S02 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- Partial derivatives, and a regression coefficient understood as a partial derivative.
- Linear algebra geometrically: projection, rotation, rank and rank deficiency; collinearity in nutrition data as a rank problem.
- Solving simple ODEs analytically; direction fields; stability of an equilibrium in one dimension.
- Maximum likelihood as an optimisation problem; the log-likelihood surface and its curvature.
- Numerical methods: why a solver diverges, step size and stability, numerical integration.

**Skills to demonstrate**

- Derive a maximum likelihood estimator for a simple model and explain its standard error from curvature.
- Diagnose a collinearity problem as rank deficiency rather than as a variance-inflation number.

**Build target.** A dietary pattern analysis where you show, in linear algebra terms, why one component was unstable.

**Gate to the next rung.** You can explain to a colleague what their regression coefficient is a derivative of.

### S02 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- Systems of ODEs: equilibria, Jacobian, stability classification, phase portraits, bifurcation.
- Constrained optimisation: Lagrange multipliers, linear programming, shadow prices.
- Information theory at reading level — AIC as expected Kullback-Leibler divergence — and game theory at reading level, enough to see why voluntary industry self-regulation predictably fails.
- Graph and network concepts sufficient to read a DAG, a supply chain and a social network as the same object.

**Skills to demonstrate**

- Write a system of differential equations for a stated verbal theory, find its equilibria, classify their stability, and say what observation would falsify the structure.
- Set up and solve a constrained minimum-cost diet problem meeting Indian nutrient requirements, and interpret the shadow prices.
- Read a matrix equation and say what it does geometrically.

**Build target.** A least-cost diet optimisation on Indian consumption data, written up to publishable standard.

**Gate to the next rung.** You can take a colleague's hand-waved feedback story to equilibria, stability and a named parameter worth measuring, in one sitting.

---

# Part 2 · Statistical inference and modelling

## S03 · Probability and statistical inference

**Target level: Expert** — originate and adjudicate · *Prerequisites: S02* · *Part 2 · Statistical inference and modelling* · *Source: Layer 2*

**Why this level.** Most Indian MD theses treat statistics as a service to be outsourced after data collection. Owning it is the single clearest comparative advantage available inside a Community Medicine department, and you will be teaching it for thirty years. Expert here means you can teach inference without notes and adjudicate a dispute between two statisticians.

**What it buys you in real life.** It is the substrate for everything downstream — causal inference, measurement error, Bayesian small-area work, economic modelling. It is also how you stop being the person who is told what the analysis found and start being the person who decides what it found.

**The ladder — 4 rungs.** Complete each rung, including its build target, before starting the next.

### S03 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- Probability axioms, conditional probability, independence, Bayes' theorem.
- Random variables, expectation, variance, covariance; the common distributions and what generates each.
- The difference between a population parameter, a sample statistic and an estimator.

**Skills to demonstrate**

- Compute and interpret a conditional probability, including the base-rate case that defeats most clinicians.
- Say, for any reported number, whether it is a parameter, an estimate or a prediction.

**Build target.** A teaching handout on Bayes' theorem built around a diagnostic-testing example from your own clinic.

**Gate to the next rung.** You can correct the prosecutor's fallacy in a colleague's reasoning on the spot.

### S03 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- The sampling distribution as the central object of frequentist inference, not as a technicality.
- What a confidence interval is and precisely is not; what a p-value is conditional on.
- Why failure to reject is not evidence of absence.
- Likelihood: construction, maximisation, and the likelihood ratio test.

**Skills to demonstrate**

- Simulate a sampling distribution and use the simulation as your explanation rather than a formula.
- State, for any published analysis, exactly what the reported interval is conditional on.
- Identify a paper that has claimed absence of effect from a non-significant result.

**Build target.** A simulation-based teaching notebook that builds a sampling distribution from scratch, used in one resident session.

**Gate to the next rung.** You never again describe a 95% interval as containing the true value with 95% probability.

### S03 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- The exponential family and why it unifies the generalised linear model.
- Curvature of the log-likelihood as the standard error; profile likelihood.
- Equivalence testing and interval-based absence claims against a minimal important difference.
- Frequentist and Bayesian answers to the same question, and where they diverge.

**Skills to demonstrate**

- Construct an equivalence or minimal-important-difference argument instead of a null-rejection argument, and defend it to a reviewer who wants a p-value.
- Derive a profile likelihood interval and explain why it differs from a Wald interval.
- Design an analysis around precision rather than significance.

**Build target.** One analysis of your own reported with a pre-specified minimal important difference and no significance testing at all.

**Gate to the next rung.** A reviewer accepts an absence claim you made, on the basis of the interval you supplied.

### S03 · Rung 4 — Expert (originate and adjudicate)

**Concepts to understand**

- Inference as a coherent framework rather than a toolbox: what is being conditioned on in each paradigm, and what each licenses.
- The teaching sequence that takes a resident from probability to likelihood to sampling distribution without a leap of faith.
- The historical and philosophical disputes well enough to explain why the field disagrees rather than to take a side.

**Skills to demonstrate**

- Teach inference to residents, without notes, using one worked example carried all the way through.
- Adjudicate a dispute between two statisticians about an analysis and have your judgement accepted.
- Referee the statistical section of any paper in your field.

**Build target.** A taught statistics module for your department, released openly, with the simulation code.

**Gate to the next rung.** Another department sends you their thesis analyses for statistical review.

---

## S04 · Regression modelling for health outcomes

**Target level: Expert** — originate and adjudicate · *Prerequisites: S03* · *Part 2 · Statistical inference and modelling* · *Source: Layer 2 (GLM, survival)*

**Why this level.** This is your daily instrument. Expert is justified not because regression is hard but because you will teach it, referee it, and be the person other departments bring their broken models to.

**What it buys you in real life.** Every paper you write and most you review. Also, a large fraction of the corrective literature you could publish on other people's data consists of nothing more exotic than using the right effect measure and the right time origin.

**The ladder — 4 rungs.** Complete each rung, including its build target, before starting the next.

### S04 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- Linear regression as a conditional mean; what a coefficient means and what it does not.
- Binary outcomes and why linear regression misbehaves on them; the logistic link.
- Odds ratio, risk ratio and risk difference as three different numbers.

**Skills to demonstrate**

- Fit and interpret linear and logistic models and state the scale of every coefficient.
- Convert between effect measures and say when the conversion is not legitimate.

**Build target.** A reanalysis of one published table reporting odds ratios, restated as absolute risks for a policy reader.

**Gate to the next rung.** You never report an odds ratio to a non-technical audience without the absolute risk beside it.

### S04 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- The GLM as one object with three parts — random component, linear predictor, link — rather than a list of named tests.
- Poisson and negative binomial models; overdispersion and when it forces your hand.
- Time-to-event basics: hazard, censoring, Kaplan-Meier, and why person-time is not the same as persons.
- Continuous exposures: why categorising throws away information and manufactures thresholds.

**Skills to demonstrate**

- Choose the right GLM family and link for a given outcome and defend the choice.
- Fit a Cox model and check proportional hazards.
- Model a BMI exposure with splines and present the exposure-response curve.

**Build target.** One analysis of your own in which the exposure is modelled continuously and the threshold question is answered from the curve.

**Gate to the next rung.** You can explain to a colleague why their categorised BMI analysis found a threshold that is not there.

### S04 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- Competing risks, time-varying exposure and immortal time bias as design faults visible in the model specification.
- Model specification as a scientific decision: the difference between a model built for prediction and one built to estimate a specified contrast.
- Cumulative hazard, absolute risk over time, and why these communicate better than a hazard ratio.

**Skills to demonstrate**

- Fit, diagnose, present and defend each GLM and survival model on your own data, choosing the effect measure by audience.
- Spot immortal time bias and competing-risk misuse in someone else's obesity cohort paper.
- Report a survival analysis as risk over time rather than as a single ratio.

**Build target.** A published reanalysis or correspondence identifying a time-origin or effect-measure error in an existing obesity paper.

**Gate to the next rung.** You can name the time origin, censoring assumption and competing risks of any published Cox model on BMI and mortality.

### S04 · Rung 4 — Expert (originate and adjudicate)

**Concepts to understand**

- The unifying structure: why every model in this subject is a choice of likelihood plus a choice of link plus a choice of contrast.
- Where the standard implementations break, and what to do instead.
- The teaching path that takes a resident from a t-test to a GLM without their ever meeting a lookup table of named tests.

**Skills to demonstrate**

- Teach regression as one object, without notes, to a resident cohort.
- Referee the modelling section of any submitted paper in the field.
- Be the person another department brings a broken model to.

**Build target.** A departmental regression teaching module plus a reproducible worked example on Indian survey data.

**Gate to the next rung.** Residents you taught stop asking which test to use and start asking what contrast they want.

---

## S05 · Clustered, longitudinal, hierarchical and small-area models

**Target level: Advanced** — execute and defend · *Prerequisites: S04* · *Part 2 · Statistical inference and modelling* · *Source: Layer 2*

**Why this level.** Repeated anthropometry, cluster-randomised delivery, and district-level estimation are the three shapes your data will actually take. You must be able to run these yourself; you do not need to develop the estimators.

**What it buys you in real life.** District estimates are the single most-requested product from a Community Medicine department, and they are almost always produced badly. Doing them properly, with uncertainty, and explaining to a collector what they do and do not license, is both a service and a publication stream.

**The ladder — 3 rungs.** Complete each rung, including its build target, before starting the next.

### S05 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- Why observations within a cluster or within a person are not independent, and what pretending otherwise does to standard errors.
- ICC and design effect as concepts.
- Repeated measurements versus change scores.
- What a prior is, in one sentence, and that Bayesian output is a distribution rather than a point.

**Skills to demonstrate**

- Recognise clustered or repeated data on sight and say why a standard regression is wrong for it.
- Read a multilevel results table and say what the random effect represents.

**Build target.** A re-analysis of a clustered dataset showing the standard errors before and after accounting for clustering.

**Gate to the next rung.** You can explain to a colleague why their school-based study has fewer effective observations than children.

### S05 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- Random effects versus GEE, and precisely which question each answers — conditional versus marginal contrasts.
- How ICC is estimated, and how badly it is usually guessed at design stage.
- Growth-curve and trajectory models for BMI over time.
- Priors, posterior, conjugacy for intuition; MCMC and HMC behaviour; divergence diagnostics; posterior predictive checks.

**Skills to demonstrate**

- Fit multilevel models in lme4 or nlme and interpret both fixed and random parts.
- Fit a simple hierarchical Bayesian model in brms and interpret the posterior honestly, including its dependence on the prior.
- Run and present posterior predictive checks as a routine validity step.

**Build target.** A BMI trajectory analysis on repeated anthropometry, fitted both conditionally and marginally, with the difference explained.

**Gate to the next rung.** You can state which of a conditional or marginal estimate your audience actually needs, and why.

### S05 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- Hierarchical shrinkage as the right answer both to small-area estimation and to multiplicity.
- Small-area estimation methods and their assumptions; what sparse district data can and cannot support.
- Model comparison and checking in a Bayesian workflow; where the prior is doing the work.

**Skills to demonstrate**

- Produce district-level obesity estimates with uncertainty from national survey data and state the three largest threats to their validity.
- Design and power a cluster randomised trial with a defensible, sourced ICC rather than an invented one.
- Explain a shrunk estimate to a district officer who believes their district's raw number.

**Build target.** A district-level estimated map with credible intervals for one Indian state, delivered to the state programme.

**Gate to the next rung.** You correctly refuse to rank two districts whose intervals overlap, in front of someone who wants the ranking.

---

## S06 · Evidence synthesis and meta-analysis

**Target level: Advanced** — execute and defend · *Prerequisites: S04* · *Part 2 · Statistical inference and modelling* · *Source: Layer 2 Working*

**Why this level.** A systematic review is one of the few high-value outputs fully achievable during residency, and synthesis skill is what lets you make an authoritative claim about a literature rather than an impression of it.

**What it buys you in real life.** It converts reading into a citable asset, and it is the natural companion output to any grant application, because a good review establishes the gap you propose to fill.

**The ladder — 3 rungs.** Complete each rung, including its build target, before starting the next.

### S06 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- What a systematic review is and how it differs from a narrative review.
- The PRISMA flow and why screening is done in duplicate.
- Effect measures pooled on the right scale; the forest plot read correctly.

**Skills to demonstrate**

- Screen and extract to a written protocol without drifting.
- Read a forest plot and say what the diamond represents.

**Build target.** A registered review protocol on PROSPERO for a question you have checked is unanswered.

**Gate to the next rung.** You can state, before starting, who is waiting for this review's answer.

### S06 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- Fixed versus random effects and what each assumes about the underlying effect distribution.
- Heterogeneity and its routine misinterpretation: I-squared is not a measure of absolute variation; prediction intervals are.
- Small-study effects and funnel asymmetry, which is not synonymous with publication bias.
- Risk-of-bias assessment as structured judgement; GRADE as a communication device with known weaknesses.

**Skills to demonstrate**

- Run a full synthesis in metafor: pool, assess heterogeneity, present a prediction interval alongside every random-effects summary.
- Assess risk of bias and carry it into the conclusion rather than reporting it separately.

**Build target.** One completed systematic review and meta-analysis, submitted, reporting prediction intervals.

**Gate to the next rung.** Your summary estimate is never quoted without its prediction interval, because you never present it that way.

### S06 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- Network meta-analysis and its transitivity assumption; dose-response meta-analysis.
- Individual participant data meta-analysis as the gold standard, and what it costs to obtain.
- Meta-regression, its low power, and the ecological fallacy at study level.

**Skills to demonstrate**

- Conduct a dose-response or network synthesis and defend the assumptions that make it interpretable.
- Judge whether a proposed review question is genuinely unanswered before committing months to it.
- Referee a submitted meta-analysis.

**Build target.** A synthesis that changes what a guideline committee would write, not just what a reader knows.

**Gate to the next rung.** A guideline group cites your review as the basis for a recommendation.

---

## S07 · Prediction modelling and machine learning

**Target level: Intermediate** — read, critique and commission · *Prerequisites: S04* · *Part 2 · Statistical inference and modelling* · *Source: Layer 2 Working*

**Why this level.** Deliberately capped. Most "AI for obesity" work is prediction dressed as insight, and your differentiation lies in causal and measurement work, not in model tuning. You need enough to supervise a collaborator, referee a paper, and refuse a bad proposal — not enough to compete with a data science group.

**What it buys you in real life.** The ability to say no, with reasons, to the steady stream of proposals to apply machine learning to a dataset that cannot support a causal claim — and to say yes intelligently when prediction genuinely is the task, as in triage or screening prioritisation.

**The ladder — 2 rungs.** Complete each rung, including its build target, before starting the next.

### S07 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- Prediction and explanation as different tasks with different success criteria.
- Training, validation and test data; what overfitting is.
- Discrimination and calibration as two separate properties, and why AUC alone is an inadequate report.

**Skills to demonstrate**

- Read a risk-score paper and say whether it was externally validated and whether calibration was reported.
- Notice when a predictive model's variable importance is being described in causal language.

**Build target.** A written critique of one published obesity or diabetes risk score used in India.

**Gate to the next rung.** You can explain to a colleague why their high AUC does not mean the model is usable in their clinic.

### S07 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- Regularisation and the bias-variance trade-off; cross-validation done without leakage.
- Why scores developed elsewhere transfer poorly to South Asian populations, and what external validation requires.
- TRIPOD reporting and what a competent prediction paper must contain.
- The honest position that most AI-for-obesity work is prediction dressed as insight.

**Skills to demonstrate**

- Fit a regularised model and a gradient-boosted model yourself, well enough to know what you are commissioning.
- Specify to a collaborator the outcome definition, validation design and reporting standard you require, and judge whether they delivered.
- Decline a machine-learning proposal on a dataset that cannot support the claim, with reasons.

**Build target.** One commissioned or supervised prediction analysis where you wrote the specification and signed off the validation.

**Gate to the next rung.** You can tell, in one reading, whether a paper's model is a risk score or a causal claim wearing one.

---

# Part 3 · Measurement science

## S08 · Measurement error theory and correction

**Target level: Expert** — originate and adjudicate · *Prerequisites: S03, S04* · *Part 3 · Measurement science* · *Source: Layer 2 measurement — the signature area*

**Why this level.** Measurement error is the central methodological problem of nutrition and obesity epidemiology, and mastering it is the single highest-return specialised investment available to you. True diet-disease relative risks mostly sit between 1.05 and 1.3 while error, confounding and selection each generate bias of similar magnitude — so a field-wide capability to quantify error is worth more than another association study. This is also the layer that makes corrective reanalysis of other people's data a permanent publication stream.

**What it buys you in real life.** It is the fastest route from "another Indian cross-sectional study" to methodological authority, and it is the skill that lets you referee the nutrition literature rather than be moved by it. It also protects your own cohort from producing attenuated estimates nobody can interpret.

**The ladder — 4 rungs.** Complete each rung, including its build target, before starting the next.

### S08 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- Every measurement contains error, and error is not the same as bias.
- Random versus systematic error, illustrated on a weighing scale and on a 24-hour recall.
- Under-reporting of intake as the single most reliable finding in dietary assessment, and that it is not uniform across people.

**Skills to demonstrate**

- Identify, for any exposure in a paper, how it was measured and whether the authors treated it as error-free.
- Say why a self-reported intake mean cannot be taken at face value.

**Build target.** A written note on how every exposure in your own thesis was measured and what error each carries.

**Gate to the next rung.** You never again describe a self-reported exposure without naming its error structure.

### S08 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- Classical and Berkson error models, and why dietary self-report violates both by having person-specific bias correlated with body size.
- Attenuation of effect estimates under non-differential error.
- The two counterintuitive results: differential error can bias away from the null, and error in a confounder causes residual confounding that no adjustment repairs.
- Reliability and agreement: ICC, Bland-Altman, why a correlation coefficient is a bad way to validate an instrument, kappa and its base-rate dependence.

**Skills to demonstrate**

- Say, qualitatively, which direction a given error structure will push an estimate.
- Critique a validation study that reported correlation instead of agreement.
- Read Keogh and White's tutorial papers and follow the algebra.

**Build target.** A Bland-Altman reanalysis of an instrument-validation paper that reported only correlation.

**Gate to the next rung.** You can predict the direction of bias from the error structure before seeing the result.

### S08 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- Regression calibration and the NCI method for usual intake distributions; SIMEX.
- Validation and calibration substudy design, and what each buys per rupee.
- Recovery biomarkers and what each recovers: doubly labelled water for energy, 24-hour urinary nitrogen for protein, urinary sodium and potassium.
- Energy adjustment — residual method, nutrient density, multivariate nutrient density — and what causal question each actually answers.

**Skills to demonstrate**

- Apply regression calibration or the NCI method to a real dietary dataset in R (simex, mecor) and defend the correction to a reviewer.
- Design and cost the validation substudy that would settle a specific attenuation question.
- Choose and justify an energy adjustment method by the question rather than by convention.

**Build target.** A corrected reanalysis of one of your own or a public dietary dataset, reporting uncorrected and corrected estimates side by side.

**Gate to the next rung.** You can state the plausible corrected range for an observed association of 1.2, with the assumptions written down.

### S08 · Rung 4 — Expert (originate and adjudicate)

**Concepts to understand**

- Joint quantitative bias analysis: unmeasured confounding, misclassification and selection handled simultaneously rather than one at a time.
- The field-level implication that true diet-disease relative risks of 1.05 to 1.3 sit inside the field's own bias envelope.
- Where the standard correction methods themselves fail, and what assumptions you are trading.

**Skills to demonstrate**

- Take any published nutritional epidemiology paper and state quantitatively how much of its association measurement error alone could explain.
- Teach measurement error to residents without notes, using one dataset carried through.
- Referee the measurement section of any nutrition paper and be the person whose judgement settles it.

**Build target.** A published methodological paper or corrective reanalysis built on measurement error, plus a taught module.

**Gate to the next rung.** Another group sends you their validation design for review before they field it.

---

## S09 · Measurement instruments: body composition, expenditure, diet, activity, sleep

**Target level: Expert** — originate and adjudicate · *Prerequisites: S01, S08* · *Part 3 · Measurement science* · *Source: Layer 1 Physics (Working); Layer 2 instrument science*

**Why this level.** Every exposure and outcome you will ever study arrives through one of these instruments, and in India most field studies use the cheapest of them while reporting the precision of the most expensive. Instrument fluency plus validation capability is what makes you the person a collaborator must consult before designing anything.

**What it buys you in real life.** Instrument validation is a Months-cost, high-enabling output: it produces a paper, and it unlocks every subsequent study that uses the instrument. For a chrononutrition programme it is the mandatory first brick.

**The ladder — 4 rungs.** Complete each rung, including its build target, before starting the next.

### S09 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- What each common instrument physically measures: a scale, a tape, a bioimpedance device, a questionnaire, an accelerometer.
- BMI as a ratio with known misclassification, and waist and waist-to-height as cheap proxies.
- That a cheap instrument reported with an expensive instrument's precision is the commonest error in Indian field studies.

**Skills to demonstrate**

- Take anthropometry correctly and repeatably, including waist at the right landmark.
- Say, for any study, which instrument produced each variable.

**Build target.** A written standard operating procedure for anthropometry in your own department, with a repeatability check.

**Gate to the next rung.** Two observers using your SOP agree within a stated tolerance.

### S09 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- Body composition models: two-, three- and four-compartment, and what each assumes.
- DXA's photon attenuation assumptions and where they fail in obesity; bioimpedance as a conductivity measurement with hydration-dependent error; air displacement plethysmography; isotope dilution for total body water.
- Indirect calorimetry: respiratory quotient, the Weir equation, what a whole-room calorimeter measures.
- Dietary instruments compared: 24-hour recall, FFQ, food records, weighed records — each with its own error structure.
- Activity and sleep instruments: accelerometry and the cut-point problem, GPAQ and IPAQ error, polysomnography, actigraphy, PSQI, Epworth.

**Skills to demonstrate**

- Explain the error structure of DXA, BIA and doubly labelled water from memory.
- Choose an instrument for a given study and budget, and state in the protocol what misclassification you are buying.
- Read a methods section and name the measurement property the authors failed to report.

**Build target.** An instrument comparison memo for one planned study, recommending a choice with the error trade-off quantified.

**Gate to the next rung.** Your protocol reviewers stop asking which instrument you used and why.

### S09 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- Doubly labelled water in detail: deuterium and oxygen-18 elimination logic, why it is the criterion method for free-living expenditure, its 5 to 8 percent error, and its cost implications for design.
- Validation study design: comparator choice, sample size for agreement, and the difference between validation, calibration and reliability.
- The specific Indian difficulty of measuring intake where food is shared from a common pot and portion estimation has no clean anchor.
- Raw-acceleration metrics (ENMO, MAD), wear-time criteria and non-wear detection as the modern alternative to cut-points.
- Consumer wearables and their validity, which matters because they are the only realistic route to scale in India.

**Skills to demonstrate**

- Design and run a validation study of a dietary or chrononutrition instrument in an Indian population, with the right comparator and the right agreement statistics.
- Process raw accelerometry from file to exposure variable in GGIR, defending every processing choice.
- Develop or adapt a dietary assessment instrument for an Indian population and document its properties.

**Build target.** One completed, published instrument validation in an Indian sample — the mandatory first brick of a chrononutrition programme.

**Gate to the next rung.** Another Indian group adopts your instrument or your processing pipeline.

### S09 · Rung 4 — Expert (originate and adjudicate)

**Concepts to understand**

- Instrument science as a coherent discipline: what it means for a measurement to be fit for a specified causal question rather than good in general.
- Where the criterion methods themselves disagree, and how the field resolves it.
- The design of a measurement protocol that a district-level study can actually execute without degrading.

**Skills to demonstrate**

- Adjudicate a dispute about whether a given instrument supports a given claim.
- Teach instrument science to residents without notes.
- Set the measurement standard for a multi-site Indian study and defend it to funders.

**Build target.** A published measurement-methods contribution plus the measurement protocol for your own cohort.

**Gate to the next rung.** You are asked to write the measurement section of someone else's protocol.

---

# Part 4 · Causal inference

## S10 · Potential outcomes, identification and target trial emulation

**Target level: Expert** — originate and adjudicate · *Prerequisites: S03* · *Part 4 · Causal inference* · *Source: Layer 2 Causal Core*

**Why this level.** Obesity research is a museum of causal errors. Mastering identification means you can publish corrective work on other people's data indefinitely, and it is the discipline that keeps your own observational work well-posed.

**What it buys you in real life.** It is the highest-yield single habit in the whole map. It improves every design you touch, it makes your protocols reviewable, and it gives you a standard critique that applies to most of the field's output.

**The ladder — 4 rungs.** Complete each rung, including its build target, before starting the next.

### S10 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- Association is not causation, stated as a structural claim rather than a slogan.
- Counterfactual thinking: what would have happened to this person under the other exposure.
- Confounding as a recognisable structure rather than a list of variables to adjust for.
- Randomisation as the device that makes the counterfactual contrast estimable.

**Skills to demonstrate**

- State the counterfactual contrast a study is trying to estimate, in words.
- Recognise when a paper has slid from association language into causal language.

**Build target.** A written counterfactual restatement of the research question in your own thesis.

**Gate to the next rung.** You can say what your own study's estimate would mean if it were causal, and why it may not be.

### S10 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- Potential outcomes formally; average treatment effect and treatment effect on the treated.
- The three identification conditions — exchangeability, positivity, consistency — stated for a specific study rather than recited.
- Consistency as the condition this field breaks: obesity is a state, not a treatment, and lowering BMI by diet, surgery, a GLP-1 agonist or lifelong lower adiposity are four different causal quantities.
- The target trial as a seven-part specification: eligibility, treatment strategies, assignment, follow-up start, outcome, causal contrast, analysis plan.

**Skills to demonstrate**

- Write the target trial table for a published observational obesity analysis.
- Identify a positivity violation in a real dataset.
- Explain to a clinical audience why the effect of obesity is not a well-defined quantity, without losing the room.

**Build target.** A written target trial specification for one published paper, circulated in journal club.

**Gate to the next rung.** You can name, for any observational obesity estimate, which of the three conditions is most in doubt.

### S10 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- How the target trial framing exposes immortal time bias and prevalent-user bias almost automatically.
- Eligibility and grace periods; when the follow-up clock starts and why it is usually wrong.
- Sustained treatment strategies versus point interventions, and which one the data can support.

**Skills to demonstrate**

- Specify the target trial for every observational analysis you design, in writing, before analysis.
- Name the one design change that would most improve a published study's identification.
- Convert a vague clinical question into a well-posed causal contrast in a protocol.

**Build target.** One of your own analyses designed, preregistered and reported explicitly as a target trial emulation.

**Gate to the next rung.** You can write a target trial table for any observational obesity paper in ten minutes.

### S10 · Rung 4 — Expert (originate and adjudicate)

**Concepts to understand**

- Identification as a claim about the world rather than about the estimator, and what follows when it fails.
- The frontier cases where target trial emulation is contested or insufficient.
- The teaching sequence that takes a clinician from association to counterfactual without losing them at the first abstraction.

**Skills to demonstrate**

- Teach the identification conditions without notes, using one obesity example throughout.
- Adjudicate whether a proposed observational analysis can answer the question its authors want answered.
- Referee causal claims across the obesity literature as a standing role.

**Build target.** A published corrective analysis built on an ill-defined-intervention critique, plus a taught module on target trial emulation.

**Gate to the next rung.** Colleagues bring you their observational questions before they collect data rather than after.

---

## S11 · Causal diagrams, structural bias and sensitivity analysis

**Target level: Expert** — originate and adjudicate · *Prerequisites: S10* · *Part 4 · Causal inference* · *Source: Layer 2 Causal Core and the obesity-specific traps*

**Why this level.** The obesity traps are structural, they recur, and each one found in someone else's data is a publishable paper. You need to draw them faster than you can explain them.

**What it buys you in real life.** A permanent, low-cost critique engine, and protection against the commonest way good Indian data produces uninterpretable results — adjusting for everything measured.

**The ladder — 4 rungs.** Complete each rung, including its build target, before starting the next.

### S11 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- A DAG as a picture of assumptions, and arrows as claims.
- Confounder, mediator and collider as three distinct roles a variable can play.
- That adjusting for everything measured is not conservative.

**Skills to demonstrate**

- Draw a simple DAG for a familiar clinical question.
- Name the role each covariate is playing in a published adjustment set.

**Build target.** A DAG for your own thesis question, drawn and shown to two colleagues for attack.

**Gate to the next rung.** You can explain why adjusting for a mediator is a mistake, using a drawing.

### S11 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- d-separation, the backdoor criterion, minimal sufficient adjustment sets, and what a DAG cannot encode.
- The four ways adjustment goes wrong: confounding, collider stratification, mediator adjustment, adjustment for a proxy of the outcome.
- Selection bias as structural bias rather than a sampling annoyance.
- The named obesity traps: the obesity paradox, reverse causation, depletion of susceptibles, time-varying confounding, the ill-defined intervention.

**Skills to demonstrate**

- Draw the DAG for collider stratification and use it to explain the obesity paradox to a mixed clinical audience.
- Derive a minimal adjustment set in dagitty and justify every variable included and excluded.
- Identify which of the four adjustment failures a given paper has committed.

**Build target.** A journal-club series in which each session diagnoses one obesity trap in a real paper.

**Gate to the next rung.** You can draw each of the four adjustment failures in under a minute, from memory.

### S11 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- The frontdoor criterion and where it is usable.
- Sensitivity analysis as a first-class result: E-values, bounds, negative control exposures and outcomes.
- Quantitative bias analysis handling unmeasured confounding, misclassification and selection simultaneously.
- Transportability and generalisability: why a UK Biobank estimate does not transfer to rural Chhattisgarh, and the formal machinery for reasoning about it.

**Skills to demonstrate**

- Perform joint quantitative bias analysis and report it as a headline result rather than a supplement.
- State an E-value for your own findings before a reviewer asks.
- Use negative controls to test a suspected unmeasured confounding structure.

**Build target.** One published analysis where the bias analysis is in the main results and changes the interpretation.

**Gate to the next rung.** Your reviewers stop asking you to adjust for mediators, because your DAG already answered them.

### S11 · Rung 4 — Expert (originate and adjudicate)

**Concepts to understand**

- Structural causal models and interventional calculus beyond the backdoor criterion.
- Causal discovery algorithms and why they underperform on real epidemiological data.
- Interference and spillover, which matters for community-level nutrition interventions where neighbours' behaviour affects yours.
- The limits of graphical reasoning and where it must hand over to design.

**Skills to demonstrate**

- Adjudicate a dispute about an adjustment set and have your judgement accepted.
- Teach structural bias to residents without notes, drawing each trap live.
- Find an obesity trap in someone else's data and publish the correction — a repeatable output stream.

**Build target.** At least one published paper whose contribution is a structural-bias correction to an existing literature.

**Gate to the next rung.** The obesity paradox explanation that circulates in your institution is yours.

---

## S12 · G-methods, time-varying treatment and mediation

**Target level: Advanced** — execute and defend · *Prerequisites: S10, S11, S04* · *Part 4 · Causal inference* · *Source: Layer 2 Causal Working*

**Why this level.** Any longitudinal analysis of weight, treatment and outcome has time-varying confounding by construction: weight affects treatment which affects weight. Standard adjustment is wrong here, and you must be able to do it right yourself.

**What it buys you in real life.** It is the correct machinery for evaluating GLP-1 use, weight-loss programmes, and any exposure that people move in and out of over time — which is the shape of nearly all the questions worth asking about the current Indian drug market.

**The ladder — 3 rungs.** Complete each rung, including its build target, before starting the next.

### S12 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- Why adjusting for a variable that is both a confounder and affected by prior treatment is wrong in both directions.
- Standardisation as averaging over a covariate distribution.
- Weighting as a way of constructing a pseudo-population.

**Skills to demonstrate**

- Recognise a time-varying confounding structure in a longitudinal design.
- Compute a simple standardised estimate by hand.

**Build target.** A DAG of one longitudinal weight-management dataset showing the feedback between weight, treatment and outcome.

**Gate to the next rung.** You can say why baseline adjustment is not enough for a weight-loss programme evaluation.

### S12 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- The g-formula and inverse probability weighting; why they agree in simple cases and diverge in interesting ones.
- Marginal structural models and stabilised weights; positivity violations in practice and what truncation costs.
- Mediation in the counterfactual framework: controlled direct effects, natural direct and indirect effects, and the cross-world assumption.

**Skills to demonstrate**

- Fit an MSM with stabilised weights and diagnose the weight distribution.
- Implement the parametric g-formula for a sustained-strategy contrast and present it as risk over time.
- Decompose a mediated effect and state the assumption that makes the decomposition meaningful.

**Build target.** One longitudinal analysis of your own fitted with g-methods and reported against a naive adjusted estimate.

**Gate to the next rung.** You can explain to a reviewer, in a paragraph plus a DAG, why baseline adjustment was insufficient.

### S12 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- Doubly robust estimation; targeted maximum likelihood or double machine learning learned properly, as table stakes in serious epidemiology.
- G-estimation of structural nested models and when it is preferable.
- Where machine learning belongs inside a causal estimator and where it does not.

**Skills to demonstrate**

- Implement one doubly robust estimator end to end and defend the nuisance model choices.
- Evaluate a GLP-1 treatment question with time-varying exposure and report it as a sustained-strategy contrast.
- Referee a submitted paper using g-methods.

**Build target.** A published analysis of a time-varying obesity treatment using g-methods, with code released.

**Gate to the next rung.** A methods-literate reviewer accepts your weight diagnostics without further questions.

---

## S13 · Instrumental variables and Mendelian randomisation

**Target level: Advanced** — execute and defend · *Prerequisites: S10, S11* · *Part 4 · Causal inference* · *Source: Layer 2 Causal Working*

**Why this level.** There is an enormous MR literature on adiposity and you will be expected to read, criticise and occasionally run it. You do not need to be a statistical geneticist; you need to be un-foolable.

**What it buys you in real life.** Genetic causal evidence is what the endocrinology and international literature increasingly runs on; being able to referee it stops you either over-trusting or reflexively dismissing it, and marks you as methodologically current.

**The ladder — 3 rungs.** Complete each rung, including its build target, before starting the next.

### S13 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- Instrumental variables as a way of using a source of variation you did not control.
- Genotype as fixed at conception and therefore unconfounded by later behaviour.
- What Mendelian randomisation claims to estimate.

**Skills to demonstrate**

- Read an MR abstract and say what exposure and outcome are being linked.
- State why an instrument must not affect the outcome except through the exposure.

**Build target.** An annotated reading of one MR paper on adiposity.

**Gate to the next rung.** You can explain MR to a clinician in three sentences without saying it proves causation.

### S13 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- The three IV assumptions — relevance, independence, exclusion restriction — for a genetic instrument specifically.
- Two-sample and two-step designs; MR-Egger, weighted median and mode-based estimators; what pleiotropy diagnostics can and cannot detect.
- Weak instrument bias, winner's curse and sample overlap.
- The problems of BMI as an MR exposure: it is a composite, instruments act through appetite and behaviour, and the contrast estimated is lifelong adiposity rather than an intervention.

**Skills to demonstrate**

- Run a two-sample MR in TwoSampleMR with the full diagnostic suite.
- Critique a published MR study on adiposity on instrument selection, pleiotropy handling and interpretive overreach.

**Build target.** One MR analysis run end to end, with assumptions stated rather than cited.

**Gate to the next rung.** You can explain why an MR estimate of the effect of BMI and a semaglutide trial answer different questions, and both are correct.

### S13 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- The thinness of South Asian GWAS coverage as both a limit on importing findings and a research opportunity.
- Non-genetic instruments in policy evaluation and how to judge their credibility.
- Triangulation: combining MR with quasi-experimental and observational evidence whose biases differ.

**Skills to demonstrate**

- Judge whether a proposed instrument in a policy evaluation is credible, and say what would break it.
- Design a triangulated analysis where MR is one of three approaches with non-overlapping biases.
- Referee the MR literature on adiposity as a standing role.

**Build target.** A triangulated paper on one adiposity exposure combining MR with at least one other identification strategy.

**Gate to the next rung.** You are invited to review MR submissions.

---

## S14 · Quasi-experimental policy evaluation

**Target level: Advanced** — execute and defend · *Prerequisites: S10, S11, S05* · *Part 4 · Causal inference* · *Source: Layer 2 Causal Working*

**Why this level.** This is the machinery by which you will evaluate actual Indian policy, and state-level variation in tax, labelling and school-food policy makes it directly usable. It must be executable by you, because the policy window will not wait for a collaborator.

**What it buys you in real life.** It is the bridge between the methods layers and the policy layers: it is how you answer "did it work?" for an instrument nobody could have randomised, and it is the output format a health secretary can act on.

**The ladder — 3 rungs.** Complete each rung, including its build target, before starting the next.

### S14 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- A policy change as a natural experiment, and the before-after comparison as its weakest form.
- Why a control group matters even when nobody randomised.
- Secular trend as the thing that ruins naive before-after claims.

**Skills to demonstrate**

- Identify a dated policy change and a plausible comparator.
- Say why a simple before-after evaluation is uninterpretable.

**Build target.** A written evaluation sketch for one recent Indian policy change, naming the comparator.

**Gate to the next rung.** You never accept a before-after prevalence claim as evidence of policy effect.

### S14 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- Difference-in-differences and the parallel trends assumption: how to argue for it and test its implications.
- Event-study plots as the standard presentation.
- Interrupted time series with and without a control series; autocorrelation; level change versus slope change.
- Regression discontinuity: identification at the cut-off, bandwidth choice, manipulation tests.

**Skills to demonstrate**

- Run a difference-in-differences evaluation of a state-level policy and defend parallel trends with evidence.
- Build an interrupted time series around a dated change, such as the 40% GST slab on carbonated beverages from 22 September 2025.
- Present an event-study plot correctly.

**Build target.** One completed quasi-experimental evaluation of an Indian state or national policy.

**Gate to the next rung.** A reviewer challenges parallel trends and your pre-trend evidence answers them.

### S14 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- Staggered adoption and the bias of two-way fixed effects, with the modern estimators that repair it.
- Synthetic control and inference by permutation.
- The structural problem that policy effects are delayed and evaluation windows are usually shorter than response times.

**Skills to demonstrate**

- Apply a modern staggered-adoption estimator and explain why the naive two-way fixed effects estimate differs.
- Pre-specify an evaluation design before a policy lands, which is the only way these designs are ever clean.
- Advise a state government on what to measure now so the policy can be evaluated later.

**Build target.** A pre-registered evaluation protocol filed before an anticipated Indian regulatory change takes effect.

**Gate to the next rung.** Your evaluation design existed before the policy did.

---

# Part 5 · Epidemiology

## S15 · Study and trial design, power and missing data

**Target level: Advanced** — execute and defend · *Prerequisites: S03, S10* · *Part 5 · Epidemiology* · *Source: Layer 3 Core; Layer 2 design*

**Why this level.** Your MD gives you the vocabulary; what it does not give you is design as a menu you choose from deliberately rather than a label applied afterwards. Every design decision you get wrong is unfixable at analysis.

**What it buys you in real life.** Design is where most Indian primary research is lost, and where a single good decision compounds for years. It is also the conversation in which you are most useful to collaborators before their money is spent.

**The ladder — 3 rungs.** Complete each rung, including its build target, before starting the next.

### S15 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- The standard design menu: cross-sectional, cohort, case-control, trial, and what each estimates.
- Bias, confounding and chance as three separate threats.
- Why sample size is a design question and not a calculation done at the end.

**Skills to demonstrate**

- Name the design of any paper you read and what parameter it estimates.
- Run a conventional sample size calculation and state its assumptions.

**Build target.** A design comparison memo for your own thesis question, with the alternatives named.

**Gate to the next rung.** You can say what your chosen design buys and what it costs, out loud.

### S15 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- The fuller observational menu: nested case-control, case-cohort, case-crossover, self-controlled case series, two-stage sampling.
- The trial menu beyond the parallel RCT: cluster randomised, stepped-wedge, factorial, non-inferiority, adaptive, pragmatic and registry-based.
- Missing data: MCAR, MAR, MNAR; multiple imputation done properly, including the requirement that the imputation model contains the outcome.
- Arguing from precision and minimal important difference rather than from significance.

**Skills to demonstrate**

- Choose and justify a design against a stated question and budget, with alternatives named and rejected for reasons.
- Implement multiple imputation in mice and report sensitivity to the missingness assumption.
- Run a simple simulation-based power analysis.

**Build target.** A protocol in which the design section names three rejected alternatives and why.

**Gate to the next rung.** Your protocol reviewers argue about your parameters rather than your design choice.

### S15 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- SMART designs for sequencing behavioural interventions, and N-of-1 designs, which are genuinely useful in obesity management and badly underused.
- Simulation-based power for clustered, longitudinal and non-standard designs.
- Design as protection: which specific bias each design choice buys protection from.

**Skills to demonstrate**

- Run simulation-based power for a clustered or longitudinal design in R.
- Design an N-of-1 or crossover study for an individual clinical question and analyse it correctly.
- Be the person collaborators consult before money is spent.

**Build target.** One study of your own using a design rarely seen in Indian NCD work — stepped-wedge, SMART, case-cohort or N-of-1.

**Gate to the next rung.** You can be handed a question and a budget and produce the design, power argument and missing-data plan in one sitting.

---

## S16 · Genetics, developmental origins and life-course epidemiology

**Target level: Expert** — originate and adjudicate · *Prerequisites: S10, S15* · *Part 5 · Epidemiology* · *Source: Layer 4 Genetics/DOHaD; Layer 3 life-course*

**Why this level.** This is India's specific story, and it is the argument that reorients obesity policy from adult treatment to adolescent and maternal nutrition. You must be able to make it from primary evidence, to a policymaker, without a slide.

**What it buys you in real life.** It is the intellectual bridge between India's undernutrition machinery — where public health capacity already exists — and its obesity problem. It is the argument that lets an obesity programme be delivered through maternal and child health rather than competing with it.

**The ladder — 4 rungs.** Complete each rung, including its build target, before starting the next.

### S16 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- Obesity runs in families, and family resemblance has both genetic and shared-environment sources.
- Birthweight and later disease as an observed association — the Barker hypothesis in outline.
- That India has a history of low birthweight and is now acquiring adult energy surplus.

**Skills to demonstrate**

- Take a three-generation family and birth history in clinic.
- State the double burden of malnutrition as one problem rather than two.

**Build target.** A written family-and-birth history proforma added to your own clinical or study intake.

**Gate to the next rung.** You ask about birthweight and childhood growth as routinely as you ask about diet.

### S16 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- Heritability: what twin and adoption studies estimate, why BMI heritability of 0.4 to 0.7 does not mean obesity is 40 to 70 percent genetic in any policy-relevant sense, and why heritability rises as environments homogenise.
- Monogenic obesity — leptin and leptin receptor deficiency, POMC, PCSK1, MC4R at roughly 1 in 300 to 1500 — and syndromic forms: Prader-Willi, Bardet-Biedl, Alström and the ciliopathy connection.
- Polygenic architecture: FTO acting through IRX3/IRX5, and the finding that most implicated genes are expressed in the central nervous system, making obesity substantially a neurobehavioural trait.
- Life-course models: critical and sensitive periods, accumulation, chains of risk.
- The Dutch Hunger Winter; fetal programming versus postnatal catch-up growth as separate mechanisms.

**Skills to demonstrate**

- Recognise the clinical triad warranting genetic testing — severe early-onset obesity, hyperphagia from infancy, consanguinity — all more findable in India than in Europe and almost entirely undiagnosed here.
- Critique a heritability claim used to argue against environmental intervention.
- Read the Indian birth cohort literature and summarise its joint finding.

**Build target.** A clinic audit of how many patients meet monogenic red-flag criteria and how many were tested.

**Gate to the next rung.** You can explain why high heritability and environmental causation are both true, to a sceptical clinician.

### S16 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- The Indian cohorts in detail: Pune Maternal Nutrition Study, Mysore Parthenon and Birth Records, New Delhi Birth Cohort, Vellore — and their joint finding that low birthweight followed by childhood or adolescent BMI gain predicts adult risk more strongly than either alone.
- Wells's capacity-load model: metabolic capacity laid down early versus metabolic load acquired later.
- Gene-environment interaction and its policy-useful reverse framing — environmental improvement reduces the penetrance of genetic risk.
- Polygenic risk scores: construction, calibration, and poor transfer from European-ancestry cohorts to South Asians.
- Epigenetics handled honestly: methylation differences associated with adiposity are mostly consequences, as MR has shown; transgenerational inheritance in humans is unproven.
- Maternal obesity, gestational diabetes and the intergenerational cycle; the confounding problems in the breastfeeding literature.

**Skills to demonstrate**

- Distinguish accumulation from critical-period models in a real dataset rather than asserting one.
- Critique a PRS paper for ancestry transferability.
- Analyse a life-course exposure sequence with the appropriate modelling rather than sequential adjustment.

**Build target.** A life-course analysis on an Indian cohort or on LASI, testing competing life-course models against each other.

**Gate to the next rung.** You can say which life-course model your data supports, and what would have distinguished them if it did not.

### S16 · Rung 4 — Expert (originate and adjudicate)

**Concepts to understand**

- The capacity-load frame as an organising theory for Indian metabolic health, including where it is contested.
- How the developmental argument reorients policy from adult treatment to adolescent and maternal nutrition — and why that places obesity prevention inside existing Indian public health capacity.
- The open questions: paternal contribution, rare variant and exome work, animal models of programming and their translational limits.

**Skills to demonstrate**

- Explain to a policymaker why India will face a larger diabetes burden than Europe at the same BMI distribution, and why that argues for acting on adolescent and maternal nutrition.
- Teach the capacity-load model without notes, at three depths.
- Adjudicate between developmental and contemporary-environment explanations for an observed Indian pattern.

**Build target.** A published paper or authoritative review establishing the Indian developmental argument, plus the policy brief version.

**Gate to the next rung.** A secretary who entered the room believing obesity is an adult lifestyle problem leaves asking about adolescent girls.

---

## S17 · Social epidemiology, equity measurement and surveillance in India

**Target level: Advanced** — execute and defend · *Prerequisites: S15* · *Part 5 · Epidemiology* · *Source: Layer 3 Core*

**Why this level.** Equity is the frame in which Indian health policy is argued, and the social gradient in obesity is the most important single empirical fact about the condition in this country. You must be able to measure it correctly yourself.

**What it buys you in real life.** It is the difference between "obesity is rising in India" and a statement a policymaker can act on. It also protects you from the commonest advocacy error — proposing an intervention that will widen the gradient.

**The ladder — 3 rungs.** Complete each rung, including its build target, before starting the next.

### S17 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- Socioeconomic position as a construct with multiple measures, not a single variable.
- The social gradient in disease, and that its direction can differ between settings.
- Equity as a distributional question distinct from an average effect.

**Skills to demonstrate**

- Describe an outcome by wealth quintile, urban-rural and sex, correctly.
- Say which SES measure a survey used and what it captures.

**Build target.** A stratified descriptive table of obesity prevalence for one state, by three SES measures.

**Gate to the next rung.** You notice when a national average is hiding a reversed gradient.

### S17 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- Indian SES measurement specifically: consumption quintiles, wealth index construction and its limitations, caste and class as distinct constructs, urban-rural classification and the peri-urban middle that most surveys handle badly.
- The social gradient in obesity and its reversal with development — in India still positive in many states and already inverted in others, which is the most important single empirical fact about obesity in the country.
- Equity metrics: concentration index, slope and relative indices of inequality, and what each is sensitive to.
- Surveillance versus research; STEPS methodology; sentinel versus population surveillance.
- Screening theory: sensitivity, specificity, predictive values, ROC, lead time and length bias, overdiagnosis.

**Skills to demonstrate**

- Compute and present a concentration index and a relative index of inequality on NFHS data, by state.
- Compute predictive values at realistic Indian prevalence and argue the population BMI screening case in both directions.
- Read a surveillance system and identify its data quality weak point.

**Build target.** A state-by-state mapping of the direction of the social gradient in obesity, with the inversion explained.

**Gate to the next rung.** You can state, for any proposed intervention, whether it is likely to be equity-neutral, improving or worsening.

### S17 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- Intervention-generated inequality as a design consideration rather than a post-hoc finding.
- Spatial epidemiology: clustering, spatial autocorrelation, GIS basics, small-area mapping.
- How to build a surveillance system that survives a change of district officer — ownership, simplicity, and a data quality audit built in.

**Skills to demonstrate**

- Design and field a surveillance instrument with an explicit data quality audit.
- Produce a spatially smoothed small-area map and interpret it responsibly.
- Advise a state on an equity-protective design change before a programme launches.

**Build target.** A functioning surveillance or monitoring instrument adopted by a district or state programme.

**Gate to the next rung.** A surveillance system you designed is still running after the officer who commissioned it has moved.

---

## S18 · Nutritional epidemiology and its pathologies

**Target level: Expert** — originate and adjudicate · *Prerequisites: S08, S10, S11, S15* · *Part 5 · Epidemiology* · *Source: Layer 3 pathologies; Layer 5 nutrition epistemics*

**Why this level.** This subject is your critical apparatus for an entire literature, and it is where a community physician who has mastered measurement and causal inference has an unfair advantage over the field's incumbents. Expert means you can adjudicate a dispute between two nutrition researchers and be right.

**What it buys you in real life.** It is what makes you useful in a guideline room rather than decorative in one, and it is the basis of the corrective-reanalysis publication stream that will keep your output steady during years when primary data collection is slow.

**The ladder — 4 rungs.** Complete each rung, including its build target, before starting the next.

### S18 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- Diet-disease associations are typically small, in the 1.05 to 1.3 relative risk range.
- Self-reported diet is measured with large error, and people who report eating well differ in many other ways.
- Diet is a composition: eating more of one thing means eating less of another.

**Skills to demonstrate**

- Ask instead of what before evaluating any dietary claim.
- Identify healthy-user bias in a published cohort finding.

**Build target.** A written critique of one widely reported diet-disease headline.

**Gate to the next rung.** You can explain to a journalist why a 20 percent risk reduction from a food frequency questionnaire is fragile.

### S18 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- The signal-to-noise problem stated quantitatively: measurement error, confounding and selection each generate bias of similar magnitude to the effects being reported.
- Healthy-user and healthy-adherer bias, and why adjustment for measured SES does not fix it.
- Compositional constraint: every dietary effect estimate is implicitly a substitution effect and the substitution must be specified.
- Vibration of effects and the garden of forking paths; specification-curve analysis and preregistration as the answers.
- Industry funding effects operating through question selection and framing rather than fabrication — and why reflexive dismissal on funding grounds is itself a failure of rigour.

**Skills to demonstrate**

- Run a specification-curve analysis on a nutrition dataset and present the distribution of defensible estimates rather than one.
- Specify the substitution explicitly in your own analyses.
- Judge a funded study on method rather than on funder.

**Build target.** A specification-curve reanalysis of one published Indian nutrition finding.

**Gate to the next rung.** You can show that a published association spans null to substantial across defensible specifications.

### S18 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- Non-replication with trials: where large dietary RCTs exist they frequently contradict the observational literature, and each divergence must be understood case by case rather than by picking a side.
- The ecological-individual gap: country-level associations with food supply are strong while individual-level associations are weak, both can be right, and the resolution is causal-structural rather than statistical.
- The structural epistemics: long-term dietary RCTs with hard outcomes are nearly impossible, so the field runs on observational data plus short-term mechanistic trials — which explains most of its instability.
- Controlled feeding studies as the underused high-value design: small, expensive, causally clean, answerable within a residency, and almost absent from the Indian literature.
- Guidelines as committee products under constraint, including political constraint about domestic agriculture.

**Skills to demonstrate**

- Read any nutrition guideline recommendation and reconstruct, from the cited evidence, whether it is supported, extrapolated or political.
- Design a controlled feeding study executable in an Indian institutional setting.
- Resolve an ecological-individual discrepancy structurally for a specific nutrient.

**Build target.** One controlled feeding study designed, costed and submitted for funding — or a published guideline appraisal reconstructing the evidence chain.

**Gate to the next rung.** A guideline committee asks you to appraise their evidence tables.

### S18 · Rung 4 — Expert (originate and adjudicate)

**Concepts to understand**

- The field's failure modes as a single coherent account rather than a list, and what would have to change for it to stabilise.
- Where your own corrective critiques could themselves be wrong.
- The teaching sequence that makes a resident sceptical of nutrition claims without making them nihilistic about nutrition.

**Skills to demonstrate**

- Adjudicate a dispute between two nutrition researchers and be right.
- Hold a position on a contested dietary question with a stated confidence level, change it when evidence moves, and explain both in one paragraph.
- Teach nutritional epistemics without notes.

**Build target.** A published methodological critique that changes how a specific Indian nutrition literature is analysed, plus a taught module.

**Gate to the next rung.** You are useful in a guideline room rather than decorative in one.

---

# Part 6 · Metabolic and appetite biology

## S19 · Integrative metabolism, insulin resistance and energy expenditure regulation

**Target level: Advanced** — execute and defend · *Prerequisites: S01* · *Part 6 · Metabolic and appetite biology* · *Source: Layer 4 Metabolism*

**Why this level.** You need depth beyond MBBS physiology so you can hold a real conversation with endocrinologists and never make a biologically impossible claim in a policy brief. You do not need to run a metabolic laboratory, so Advanced — able to use the physiology correctly and defend it to a specialist — is the right ceiling.

**What it buys you in real life.** It is what lets you explain to clinicians that a patient who lost 20 kg and regained 18 experienced a physiological outcome rather than a moral failure — with the numbers. That single explanation, delivered well and often, changes clinical culture more than any guideline.

**The ladder — 3 rungs.** Complete each rung, including its build target, before starting the next.

### S19 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- The fed, fasted and starved states and which fuel dominates in each.
- The four components of total daily energy expenditure: resting metabolic rate, thermic effect of food, exercise activity thermogenesis, non-exercise activity thermogenesis, and their relative sizes.
- Insulin as the dominant anabolic signal, at MBBS depth.

**Skills to demonstrate**

- Estimate a patient's resting metabolic rate from a predictive equation and state its error.
- Say which component of expenditure an intervention is actually targeting.

**Build target.** A worked energy expenditure breakdown for three real patients of different body sizes.

**Gate to the next rung.** You can say why RMR dominates expenditure in most people and what that implies for exercise advice.

### S19 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- Substrate metabolism integrated: glycolysis, gluconeogenesis, TCA, oxidative phosphorylation, beta-oxidation, ketogenesis, and de novo lipogenesis with its actual quantitative smallness in humans on mixed diets.
- Fuel selection and metabolic flexibility; respiratory quotient as the readout; the Randle cycle; insulin resistance as a failure of flexibility.
- Insulin action at molecular level — receptor, IRS, PI3K-Akt, GLUT4 translocation — and the tissue-specific dissociation where hepatic lipogenesis stays insulin-sensitive while glucose disposal is resistant.
- Predictive RMR equations and their error in South Asians.

**Skills to demonstrate**

- Explain metabolic flexibility and its failure to a clinical audience using RQ.
- Correct the common claim that dietary carbohydrate is converted to fat in quantitatively important amounts.
- Read a metabolic physiology paper and follow the substrate argument.

**Build target.** A teaching session on insulin resistance built from the molecular pathway up to the clinical phenotype.

**Gate to the next rung.** An endocrinologist stops simplifying their vocabulary when talking to you.

### S19 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- Adaptive thermogenesis: after weight loss, expenditure falls more than body composition alone predicts, and the effect persists for years.
- Constrained total energy expenditure — Pontzer's finding that TDEE plateaus rather than scaling linearly with activity — as the most policy-relevant finding in metabolic physiology of the last decade.
- Endocrine physiology of obesity: HPA axis, cortisol, thyroid, sex steroids, PCOS, growth hormone, with cause and consequence separated for each.
- Muscle-adipose-liver crosstalk, myokines, FGF21, and the case for skeletal muscle as a target in a low-muscle-mass population.
- At reading level: mitochondrial bioenergetics and proton leak, autophagy, brown and beige adipose tissue with an honest therapeutic ceiling, the gut microbiome literature, and the obesogen hypothesis — plausible mechanism, weak human evidence, high policy salience.

**Skills to demonstrate**

- Explain adaptive thermogenesis and constrained TDEE quantitatively, with numbers, to a room of physicians.
- Dismantle, from a heat-balance estimate, the claim that brown fat activation is a therapeutic lever in adults.
- Read the microbiome and obesogen literatures without being taken in, and say precisely what each does and does not establish.

**Build target.** A taught session that explains a 20 kg loss and 18 kg regain as a physiological outcome rather than a moral failure, with the numbers.

**Gate to the next rung.** Clinicians in your institution have stopped describing regain as non-compliance.

---

## S20 · Adipose tissue biology, ectopic fat and the South Asian phenotype

**Target level: Expert** — originate and adjudicate · *Prerequisites: S19* · *Part 6 · Metabolic and appetite biology* · *Source: Layer 4 Metabolism Core and South Asian phenotype*

**Why this level.** The South Asian phenotype is a differentiating asset available to an Indian researcher and to almost nobody else. It is also where the open, publishable question sits: how the 2025 Lancet Commission's preclinical/clinical distinction should be operationalised in India.

**What it buys you in real life.** It is the biological core of every argument you will make for why Indian obesity policy cannot be imported. It is also the content that makes a national committee want you in the room.

**The ladder — 4 rungs.** Complete each rung, including its build target, before starting the next.

### S20 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- Adipose tissue as an endocrine organ, not a storage depot.
- Visceral versus subcutaneous fat, and why waist circumference adds information over BMI.
- That South Asians carry more fat and less muscle at the same BMI, and that Indian action points are 23 and 25.

**Skills to demonstrate**

- Measure and interpret waist circumference and waist-to-height against Indian cut-offs.
- Explain to a patient why their normal BMI does not exclude metabolic risk.

**Build target.** A clinic audit comparing BMI-based and waist-based risk classification in your own patients.

**Gate to the next rung.** You classify risk by more than BMI as a matter of routine.

### S20 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- Leptin, adiponectin, resistin and inflammatory cytokines; leptin's asymmetric biology as a starvation signal more than a satiety signal, which is why leptin therapy failed in common obesity and succeeded in lipodystrophy.
- Adipocyte hyperplasia versus hypertrophy; developmental windows for adipocyte number; adipose expandability and the limited-expandability hypothesis as the bridge to ectopic fat.
- Ectopic fat and lipotoxicity across depots: visceral, subcutaneous, intrahepatic, intramyocellular, epicardial, perirenal. MASLD as the hepatic manifestation.
- Adipose inflammation: macrophage polarisation, crown-like structures, hypoxia, fibrosis, and the causal ambiguity about whether inflammation drives insulin resistance or follows it.
- The South Asian phenotype in detail: higher body fat at equal BMI, greater visceral and hepatic fat, lower lean and skeletal muscle mass, lower adiponectin, earlier insulin resistance and beta-cell failure.

**Skills to demonstrate**

- Explain the thin-fat phenotype to clinical, policy and lay audiences at three depths.
- Interpret a body composition report in a South Asian patient against the right reference.
- Argue why waist outperforms BMI for cardiometabolic risk, from mechanism.

**Build target.** A descriptive analysis of body composition or waist distribution in your own population against Indian cut-points.

**Gate to the next rung.** You can explain the phenotype without a slide, to any audience.

### S20 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- The evidence behind the Indian BMI action points of 23 and 25, and where they remain wrong.
- The 2025 Lancet Commission framework separating preclinical from clinical obesity, requiring organ dysfunction or functional limitation rather than BMI alone.
- Cut-point derivation methods and their sensitivity to outcome choice, population and prevalence.
- At reading level: single-cell adipose atlases and where the depot biology is heading.

**Skills to demonstrate**

- Derive and defend population-specific anthropometric cut-points from data rather than citing them.
- Apply the preclinical-clinical distinction to a real patient series and report what changes.
- Critique a cut-point paper on its outcome and derivation choices.

**Build target.** An empirical operationalisation of preclinical versus clinical obesity in an Indian sample — an open question whoever answers will own.

**Gate to the next rung.** You can state what an Indian BMI cut-point should be, show the data, and name the assumption someone would attack.

### S20 · Rung 4 — Expert (originate and adjudicate)

**Concepts to understand**

- The phenotype as a coherent causal account linking developmental origins, depot biology and clinical risk, including where the account is weakest.
- How India should adopt the preclinical-clinical categories, as a technical and an ethical question simultaneously.
- The research agenda the phenotype implies, and what would falsify it.

**Skills to demonstrate**

- Adjudicate a dispute about Indian cut-points or obesity definitions in a national forum.
- Teach the phenotype and the capacity-load model without notes.
- Set the operational definition used by a multi-site Indian study.

**Build target.** A published operationalisation adopted by others, or authorship on an Indian consensus statement on obesity definitions.

**Gate to the next rung.** Your definition is the one other Indian studies cite when they have to choose.

---

## S21 · Appetite, reward and the determinants of intake

**Target level: Expert** — originate and adjudicate · *Prerequisites: S19* · *Part 6 · Metabolic and appetite biology* · *Source: Layer 4 Appetite Core*

**Why this level.** This is the mechanistic core of why obesity is not a willpower problem, the layer that makes the incretin drug revolution intelligible rather than magical, and the biology that justifies environmental regulation. You will explain it hundreds of times, to audiences from residents to journalists, so it must be derivable and teachable without notes.

**What it buys you in real life.** It is the single most persuasive body of content you own for moving an audience from individual blame to environmental causation — and it does so through biology rather than ideology, which is why it works on clinicians.

**The ladder — 4 rungs.** Complete each rung, including its build target, before starting the next.

### S21 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- Appetite is regulated by the brain, not decided by the person, and hunger is a signal rather than a choice.
- Ghrelin, leptin, insulin and GLP-1 named, with their broad direction of effect.
- Satiation (meal termination) and satiety (between-meal suppression) as different things.

**Skills to demonstrate**

- Explain to a patient that hunger after weight loss is physiological.
- Name which hormone a given drug class acts on.

**Build target.** A patient-facing explanation of post-weight-loss hunger, tested on real patients.

**Gate to the next rung.** No patient leaves your clinic believing hunger is a character defect.

### S21 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- The hypothalamic melanocortin pathway: arcuate POMC and AgRP/NPY neurons, second-order MC4R neurons in the paraventricular nucleus, and the fact that loss-of-function mutations here produce the most severe human obesity known.
- Brainstem integration: nucleus tractus solitarius, area postrema, vagal afferent signalling — and why so many appetite drugs cause nausea, since satiety and emesis circuits overlap.
- The gut-brain endocrine axis in detail: GLP-1, GIP, PYY 3-36, oxyntomodulin, CCK, amylin, ghrelin — secretion stimuli, half-lives, receptor distribution, central versus peripheral action. This is the pharmacological map of the entire current drug pipeline.
- The mesolimbic reward system and the wanting versus liking distinction as dissociable systems with different neurochemistry.
- The seven manipulable determinants of intake: energy density, portion size and unit bias, eating rate and texture, hyperpalatability, protein leverage, variety and sensory-specific satiety, liquid calories.

**Skills to demonstrate**

- Describe the melanocortin pathway and the gut-brain axis from memory, on a whiteboard.
- Map a drug class onto its receptor and predict its adverse effect profile.
- Rank two proposed interventions by which manipulable determinant each acts on.

**Build target.** A teaching module mapping the current drug pipeline onto the gut-brain axis.

**Gate to the next rung.** You can explain why GLP-1 agonists cause nausea from circuit anatomy rather than from a label.

### S21 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- Nutrient sensing: hypothalamic AMPK and mTOR, fatty acid and amino acid sensing, glucose-sensing neurons.
- Learning and conditioning: cue-potentiated feeding, Pavlovian conditioning to food cues, and the dorsal-striatal shift from goal-directed to habitual control — which is why advertising works and why exposure-based environmental policy is mechanistically justified.
- The regulation debate: set point, settling point and the dual intervention point model, with strong lower-boundary and weak upper-boundary defence, which is what evolutionary reasoning predicts and what explains asymmetric weight-loss difficulty.
- The food addiction debate: Yale Food Addiction Scale, substance versus behaviour framing, what neuroimaging does and does not show, and why the framing supports product regulation while risking pathologising the eater.
- Central neuroscience of GLP-1 agonists: where semaglutide and tirzepatide act, why they reduce food reward and not only appetite, and the emerging literature on other reward-driven behaviours.

**Skills to demonstrate**

- Predict, from mechanism alone, which of two proposed interventions will produce compensatory eating.
- Design the crossover feeding study that would test that prediction.
- Apply the hyperpalatability operational definition to the Indian packaged food supply.

**Build target.** A hyperpalatability characterisation of the Indian packaged food supply, or a designed crossover feeding study on one determinant of intake.

**Gate to the next rung.** You can make a sceptical physician agree that advertising restriction is a biologically motivated intervention, using only mechanism.

### S21 · Rung 4 — Expert (originate and adjudicate)

**Concepts to understand**

- The appetite system as one integrated account from molecule to marketplace, including where the account is weakest.
- At reading level: optogenetic and chemogenetic circuit work and its translational limits; interoception and insular cortex; taste receptor genetics and its weak link to intake.
- The teaching sequence that carries an audience from circuit to policy without a leap.

**Skills to demonstrate**

- Teach the whole appetite chain without notes, at three depths for three audiences.
- Adjudicate a dispute about whether a mechanism claim supports a policy claim.
- Referee the appetite and reward literature as it bears on intervention design.

**Build target.** A widely used teaching module on appetite regulation, plus a published commentary connecting mechanism to a specific Indian policy instrument.

**Gate to the next rung.** Your mechanistic explanation is the one other people reuse when they have to make this argument.

---

# Part 7 · Clinical obesity medicine

## S22 · Clinical assessment, staging and secondary causes

**Target level: Advanced** — execute and defend · *Prerequisites: S19, S20* · *Part 7 · Clinical obesity medicine* · *Source: Layer 5 Clinical Core*

**Why this level.** Without clinical competence you are a population scientist commenting on a disease you do not treat, and Indian clinicians will discount you accordingly. Advanced means you run the consultation independently — not that you are a bariatric physician.

**What it buys you in real life.** Credibility with clinicians, which is the precondition for everything you want to say to them about populations. It also generates the case exposure that keeps the rest of the clinical layer from decaying.

**The ladder — 3 rungs.** Complete each rung, including its build target, before starting the next.

### S22 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- Height, weight, BMI and waist measured correctly and repeatably.
- The common comorbidities to ask about and the common drug causes of weight gain.
- That BMI alone is a poor basis for a management decision.

**Skills to demonstrate**

- Take a competent obesity-focused history and examination.
- List the drugs in a patient's chart that promote weight gain.

**Build target.** A structured obesity clinic proforma you use on every patient.

**Gate to the next rung.** Your history reliably surfaces weight trajectory, dieting history and drug causes.

### S22 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- The full obesity history: weight trajectory from birth, dieting and regain history, family history, medications (antipsychotics, insulin and sulfonylureas, steroids, some antiepileptics, beta blockers), sleep, eating pattern and timing, binge and night-eating behaviour, activity, psychosocial context, weight-related quality of life.
- Secondary and contributory causes: hypothyroidism, Cushing's, PCOS, hypothalamic lesions, monogenic red flags.
- Comorbidity assessment: dysglycaemia, dyslipidaemia, hypertension, MASLD with fibrosis staging, OSA, PCOS, osteoarthritis, GERD, depression, subfertility, obesity-associated cancers.

**Skills to demonstrate**

- Screen for and exclude secondary causes with the right investigations rather than a panel.
- Stage MASLD fibrosis non-invasively and act on the result.
- Produce a problem list rather than a diagnosis.

**Build target.** A completed audit of secondary-cause screening in twenty consecutive patients.

**Gate to the next rung.** You can defend every investigation you ordered and every one you did not.

### S22 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- Staging rather than classifying: the Edmonton Obesity Staging System, and the 2025 Lancet Commission framework requiring organ dysfunction or functional limitation rather than BMI alone.
- Body composition in clinical decision-making, where available, and its limits.
- What each staging system changes about management, and where they disagree.

**Skills to demonstrate**

- Independently work up an adult with obesity end to end: history, examination, anthropometry, investigations, staging, problem list, plan.
- Apply EOSS and the preclinical-clinical distinction in clinic and state what each changes.
- Recognise the monogenic red-flag triad and initiate the right referral.

**Build target.** A weekly obesity or metabolic clinic slot, running, with staged patients.

**Gate to the next rung.** You run the clinic unsupervised and your referrals are accepted without correction.

---

## S23 · Lifestyle, dietary and behavioural treatment

**Target level: Advanced** — execute and defend · *Prerequisites: S22, S27* · *Part 7 · Clinical obesity medicine* · *Source: Layer 5 Clinical Core*

**Why this level.** You will deliver this, teach it and evaluate it. The core skill is not defending a diet; it is matching a pattern to a life, and being honest about effect sizes most clinicians overstate.

**What it buys you in real life.** It is the treatment most Indian patients will actually receive, and doing it well — with correct expectations set — is the difference between a patient who returns and one who disappears into the supplement market.

**The ladder — 3 rungs.** Complete each rung, including its build target, before starting the next.

### S23 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- Energy restriction as the common mechanism behind all named diets.
- That adherence, not composition, dominates outcomes at twelve months.
- Realistic effect sizes rather than the ones patients have been promised.

**Skills to demonstrate**

- Take a diet history within Indian household food architecture.
- State to a patient what weight change is realistic, before starting.

**Build target.** A written patient-facing expectations sheet with honest numbers.

**Gate to the next rung.** Your patients can state, before starting, what weight change is realistic.

### S23 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- Reference effect sizes: intensive lifestyle intervention gives roughly 5 to 8 percent weight loss at one year with substantial regain by three to five years, with Look AHEAD, the Diabetes Prevention Program and the Indian DPP work as the anchors.
- The dietary menu: energy restriction, low carbohydrate, low fat, Mediterranean, intermittent fasting and time-restricted eating, very-low-energy diets and total diet replacement with DiRECT remission data.
- Behavioural components and which carry the effect: self-monitoring, stimulus control, problem solving, relapse prevention, motivational interviewing.
- Physical activity for maintenance rather than for loss, with resistance training weighted properly for low South Asian muscle mass.

**Skills to demonstrate**

- Construct a dietary plan inside a real Indian household's roti-sabzi-dal-rice architecture, with quantities.
- Deliver motivational interviewing competently.
- Prescribe resistance training specifically rather than recommending activity.

**Build target.** A set of three worked Indian dietary plans at different income levels, used in clinic.

**Gate to the next rung.** You can match a dietary pattern to a life rather than defending a diet.

### S23 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- Revisiting a plan against adherence rather than against a target; relapse as an expected event with a prepared response.
- Total diet replacement and remission programmes: selection, delivery and the Indian feasibility question.
- Where behavioural treatment fails and what should follow it.

**Skills to demonstrate**

- Run a full course of behavioural treatment and evaluate its delivery fidelity.
- Adapt an evidence-based programme for an Indian setting without losing its active ingredients.
- Teach behavioural treatment components to residents.

**Build target.** One delivered and evaluated lifestyle intervention with fidelity and outcome data.

**Gate to the next rung.** Patients who regain return to you rather than disappearing.

---

## S24 · Pharmacotherapy of obesity

**Target level: Advanced** — execute and defend · *Prerequisites: S21, S22* · *Part 7 · Clinical obesity medicine* · *Source: Layer 5 Clinical Core; the Indian access picture*

**Why this level.** You must know this at prescribing depth. It is also the live centre of Indian obesity right now: semaglutide's Indian patents expired on 20 March 2026 and generic entry has been very large, with prices roughly 50–60% below innovator levels and at least one multi-dose vial presentation near ₹1,290 for a starting-dose month against ₹10,850–16,400 for branded product before expiry. Tirzepatide has been available since 2025 and remains on patent.

**What it buys you in real life.** Beyond the clinic: this is where your research agenda has an open door. Nobody has good Indian data on who is taking these drugs, with what indication and supervision, with what adherence, discontinuation, out-of-pocket cost, regain, non-prescription share, or equity profile. A prospective cohort or pharmacy-and-prescription surveillance study started now would be the single highest-value research asset available to you, and it is feasible from a Community Medicine department.

**The ladder — 3 rungs.** Complete each rung, including its build target, before starting the next.

### S24 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- The available agents and what each roughly achieves.
- That these are chronic therapies and that stopping leads to regain.
- The Indian access position: semaglutide's Indian patents expired on 20 March 2026, generic entry has been very large with prices roughly 50 to 60 percent below innovator levels; tirzepatide has been available since 2025 and remains on patent.

**Skills to demonstrate**

- Counsel a patient on what a GLP-1 agonist will and will not do.
- Recognise a patient using one without supervision.

**Build target.** A written patient information sheet on GLP-1 therapy including discontinuation.

**Gate to the next rung.** No patient of yours starts one of these drugs believing it is a course rather than a therapy.

### S24 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- The agents in detail: orlistat; metformin's modest effect; phentermine-topiramate and naltrexone-bupropion where available; liraglutide; semaglutide (STEP programme, roughly 15 percent mean weight loss, SELECT cardiovascular benefit); tirzepatide (SURMOUNT, roughly 20 percent); setmelanotide for specific monogenic forms.
- Mechanisms mapped onto the gut-brain axis; dosing and escalation schedules.
- Adverse effects: gastrointestinal intolerance, gallbladder and pancreatitis signals, loss of lean mass, contraindications.
- Discontinuation and regain, which makes cost the central clinical question.

**Skills to demonstrate**

- Initiate, escalate and monitor a GLP-1 receptor agonist as routine practice, including the discontinuation conversation.
- Manage GI adverse effects and protect lean mass with concurrent resistance training and protein targets.
- Select between agents for a specific patient and defend the choice.

**Build target.** A prescribing and monitoring protocol for your clinic, with a documented discontinuation pathway.

**Gate to the next rung.** You run initiation and discontinuation conversations equally well.

### S24 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- The population questions nobody has Indian data on: who is taking these drugs, with what indication and supervision, with what adherence, discontinuation, out-of-pocket cost, regain, non-prescription share and equity profile.
- The National List of Essential Medicines as the mechanism by which generic semaglutide could become affordable at population scale.
- Pharmacovigilance and prescription surveillance methods applicable to a mass generic market.

**Skills to demonstrate**

- Design a prospective cohort or pharmacy-and-prescription surveillance study of GLP-1 use in India.
- Advise a state or insurer on coverage with the cost and discontinuation evidence attached.
- Teach GLP-1 prescribing to physicians.

**Build target.** A funded or fielded GLP-1 utilisation study — plausibly the single highest-value research asset currently available from a Community Medicine department.

**Gate to the next rung.** Your data is the source people cite for the Indian GLP-1 picture.

---

## S25 · Metabolic and bariatric surgery: selection and co-management

**Target level: Advanced** — execute and defend · *Prerequisites: S22* · *Part 7 · Clinical obesity medicine* · *Source: Layer 5 Clinical Core*

**Why this level.** Advanced applies to selection, referral and lifelong co-management, which are genuinely your responsibility. The operation itself is Introductory for you — recognise, route, and never opine on technique.

**What it buys you in real life.** It completes the treatment ladder so that you are never the person who can only offer advice, and it gives you a working relationship with surgical services — which is also where your clinical case volume will come from.

**The ladder — 3 rungs.** Complete each rung, including its build target, before starting the next.

### S25 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- The three common procedures — sleeve gastrectomy, Roux-en-Y gastric bypass, one-anastomosis gastric bypass, the last widely done in India.
- That surgery works partly through gut hormones and altered food preference, not only restriction.
- That surgery creates lifelong obligations.

**Skills to demonstrate**

- Explain the options to a patient at the level of what each involves and commits them to.
- Recognise a patient who should be discussed with a surgeon.

**Build target.** A referral checklist for bariatric assessment used in your clinic.

**Gate to the next rung.** You can describe each procedure and its main long-term obligation without notes.

### S25 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- Outcomes: diabetes remission, the STAMPEDE and SM-BOSS/SLEEVEPASS trials, mortality benefit.
- Long-term obligations in detail: micronutrient deficiency, bone loss, alcohol use disorder, post-bariatric hypoglycaemia, pregnancy timing, revisional surgery.
- The Indian practice landscape and the current insurance and Ayushman Bharat coverage position.
- Endoscopic and device therapies at reading level.

**Skills to demonstrate**

- Select and counsel a candidate, run the pre-operative assessment and hand over cleanly.
- Deliver post-operative micronutrient and bone surveillance.
- Recognise late complications and act.

**Build target.** A post-bariatric surveillance protocol running in your clinic with a patient register.

**Gate to the next rung.** A bariatric surgeon is content for you to manage their patients' medical follow-up.

### S25 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- Selection as a judgement under uncertainty: who benefits most, who is harmed, and what the evidence does not settle.
- Pregnancy after surgery, adolescent surgery, and revisional decisions as contested areas.
- The access and equity picture: who in India actually reaches surgery and who does not.

**Skills to demonstrate**

- Co-manage complex post-operative patients independently, including hypoglycaemia and nutritional failure.
- Advise on coverage policy for bariatric surgery with outcome and cost evidence.
- Teach surgical selection and follow-up to physicians.

**Build target.** A published audit or cohort of bariatric outcomes or follow-up quality in an Indian setting.

**Gate to the next rung.** You are the physician on a multidisciplinary bariatric team rather than a referrer to it.

---

## S26 · Life-stage obesity: paediatric, adolescent and pregnancy

**Target level: Advanced** — execute and defend · *Prerequisites: S16, S22* · *Part 7 · Clinical obesity medicine* · *Source: Layer 5 Clinical Core*

**Why this level.** India's obesity problem is arriving through its children — the NFHS-3 to NFHS-5 comparison shows a 288% relative rise in adolescent boys against a 91% rise in adult women — which is where both the prevention argument and the political salience sit. Anything you design for schools or adolescents can do harm, so this must be executable at a defensible standard, not read about.

**What it buys you in real life.** It places obesity prevention inside the machinery Indian public health already runs — maternal and child health, ICDS, school health — rather than requiring a new vertical programme. That is the difference between a proposal that can be funded and one that cannot.

**The ladder — 3 rungs.** Complete each rung, including its build target, before starting the next.

### S26 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- Growth references and why childhood obesity is defined against a reference rather than a fixed cut-off.
- That India's obesity problem is arriving through its children: NFHS-3 to NFHS-5 shows a 288 percent relative rise in adolescent boys against a 91 percent rise in adult women.
- That adolescent weight interventions can precipitate disordered eating.

**Skills to demonstrate**

- Plot and interpret a child's growth trajectory correctly.
- Recognise language in a school programme that risks harm.

**Build target.** A growth-charting audit in your paediatric or school contacts.

**Gate to the next rung.** You never discuss a child's weight in front of them in terms of a number alone.

### S26 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- IAP versus WHO references and the practical consequences of choosing one.
- Family-based behavioural treatment as the evidence-based core.
- Disordered eating risk in adolescents and how programme design creates or avoids it.
- Obesity in pregnancy and preconception care; GDM management; interpregnancy weight change; the intergenerational cycle.

**Skills to demonstrate**

- Assess and manage a child or adolescent with the family as the unit of intervention.
- Provide preconception and antenatal weight counselling within existing maternal health services.
- Screen an adolescent for disordered eating before starting any weight intervention.

**Build target.** A family-based treatment pathway running in your setting, with an eating-disorder safety screen built in.

**Gate to the next rung.** A psychiatrist reviewing your adolescent pathway finds nothing to change.

### S26 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- The contested move toward adolescent pharmacotherapy and surgery, held with calibrated uncertainty.
- The unresolved question of screening in Indian schools, and the case on both sides.
- How to place prevention inside the machinery Indian public health already runs — maternal and child health, ICDS, school health — rather than in a new vertical programme.

**Skills to demonstrate**

- Design a school or adolescent programme whose messaging has been tested for stigma and disordered-eating risk before deployment.
- Argue the school screening question in both directions with predictive values computed at realistic prevalence.
- Advise on adolescent pharmacotherapy with the evidence and the uncertainty stated.

**Build target.** A school or adolescent intervention designed, delivered and evaluated with harm outcomes measured alongside weight outcomes.

**Gate to the next rung.** A paediatrician, a psychiatrist and a school principal would each sign off your design.

---

# Part 8 · Nutrition science

## S27 · Nutrient science for obesity and cardiometabolic risk

**Target level: Advanced** — execute and defend · *Prerequisites: S19* · *Part 8 · Nutrition science* · *Source: Layer 5 Nutrition Core*

**Why this level.** Treat nutrition as a field with real established content surrounded by an unusually large volume of unreliable claim. The skill is not knowing more nutrition facts; it is knowing which survive scrutiny — and you must be able to defend your reading of each contested area to a specialist.

**What it buys you in real life.** It is the content base under every clinical dietary conversation, every guideline critique and every policy note on reformulation. Getting it right is also how you avoid being recruited into one of the field's tribal positions.

**The ladder — 3 rungs.** Complete each rung, including its build target, before starting the next.

### S27 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- The macronutrients, their energy densities, and what each does.
- Whole versus refined grains; free sugars versus intrinsic sugars; the main fat classes.
- That Indian vegetarian diets can meet requirements with attention to quantity, B12, iron and zinc.

**Skills to demonstrate**

- Assess a diet against requirements at the level of a clinical consultation.
- Identify the binding deficiency in a described diet rather than listing all of them.

**Build target.** Three worked diet assessments across different Indian regional patterns.

**Gate to the next rung.** You can say what is actually missing from a diet rather than what is theoretically suboptimal.

### S27 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- Protein quality and the shift from PDCAAS to DIAAS; complementarity in cereal-pulse diets.
- Carbohydrate quality: fibre types and their distinct effects, resistant starch, glycaemic index and load with an honest account of their weak predictive performance and the substantial inter-individual variability in postprandial response.
- Dietary fats: the saturated fat controversy handled through the replacement-nutrient framing, why saturated fat and mortality is a badly posed question, industrial trans fat as the clearest case of successful food regulation, and the composition of Indian cooking oils.
- Free sugars and fructose: hepatic metabolism, sugar-sweetened beverages as the best-evidenced single dietary target, and the limits of extrapolating from beverages to sugar in general.
- Sodium, potassium and blood pressure; micronutrients in obesity contexts including vitamin D's associational-but-not-trial-supported relationship with adiposity, B12, iron and the hepcidin link, iodine.

**Skills to demonstrate**

- State what any dietary recommendation is a substitution for, before evaluating it.
- Argue the saturated fat question correctly, which means refusing the question as posed and re-posing it.
- Advise on cooking oil choice from composition rather than from marketing.

**Build target.** A written appraisal of one contested macronutrient question, with the comparator specified throughout.

**Gate to the next rung.** Your first response to any macronutrient controversy is a question about the comparator.

### S27 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- Where the nutrient evidence is genuinely strong, genuinely weak, and merely conventional — held separately for each nutrient.
- The trial-observational divergences nutrient by nutrient.
- How nutrient science translates into a reformulation or labelling threshold, and where the translation loses information.

**Skills to demonstrate**

- Defend your reading of a contested nutrient question to a specialist who disagrees.
- Advise a reformulation programme on which nutrient changes are worth mandating.
- Teach nutrient science to residents without notes.

**Build target.** A published appraisal or guideline contribution on one nutrient question relevant to Indian policy.

**Gate to the next rung.** A dietitian and a cardiologist both accept your summary of the fat evidence.

---

## S28 · Ultra-processed food and the effects of processing

**Target level: Advanced** — execute and defend · *Prerequisites: S18, S21, S27* · *Part 8 · Nutrition science* · *Source: Layer 5 Nutrition Core*

**Why this level.** This is the most important live debate in nutrition policy, it is the frame in which Indian front-of-pack and marketing regulation will be argued, and the competency required is to argue both sides competently — which is Advanced, not Expert, because the underlying science is genuinely unsettled and nobody can adjudicate it yet.

**What it buys you in real life.** It is the intellectual centre of the FSSAI labelling argument and of any marketing restriction. Being the person who can state the strongest version of the opposing case is what makes your own position credible to a technical panel.

**The ladder — 3 rungs.** Complete each rung, including its build target, before starting the next.

### S28 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- What processing means, and that processed is not a synonym for unhealthy.
- NOVA as a four-category classification and what it claims.
- That ultra-processed food is the frame in which Indian labelling and marketing regulation will be argued.

**Skills to demonstrate**

- Classify a shopping basket under NOVA.
- State the UPF hypothesis in one sentence without overclaiming it.

**Build target.** A NOVA classification of one Indian household's weekly purchases.

**Gate to the next rung.** You can distinguish a processing claim from a nutrient claim in a news story.

### S28 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- Hall's controlled feeding trial as the strongest causal evidence that UPF increases ad libitum intake, and exactly what it does and does not establish.
- The substantive critiques of NOVA: category heterogeneity, poor reproducibility of classification between coders, and the difficulty of separating processing from nutrient composition.
- The candidate mechanisms, each traceable to appetite biology: energy density, hyperpalatability, eating rate, texture, low satiety per calorie.

**Skills to demonstrate**

- Classify a real Indian packaged food basket and report inter-coder reliability rather than assuming it.
- Trace a claimed UPF effect to a specific mechanism and name the design that would isolate it.
- Read the UPF literature and separate the observational from the experimental claims.

**Build target.** A NOVA classification study of the Indian packaged food supply with a measured reliability statistic.

**Gate to the next rung.** You can state which parts of the UPF case rest on one feeding trial.

### S28 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- The policy stakes in both directions: a processing-based rule is simple and enforceable but scientifically contested, while a nutrient-based rule is defensible but gameable by reformulation to just below a threshold.
- How an adaptive industry responds to each rule type.
- What evidence would resolve the debate, and why it is unlikely to be generated soon.

**Skills to demonstrate**

- Argue both sides of the UPF debate competently, in front of an audience that expects you to have a side.
- Advise a regulator on the choice between processing-based and nutrient-based rules, with the trade-off quantified.
- Referee UPF papers without reflexive alignment.

**Build target.** A published analysis of the Indian packaged food supply that informs the processing-versus-nutrient rule choice.

**Gate to the next rung.** Both an advocate and an industry scientist describe your summary of the evidence as fair.

---

## S29 · Indian dietary patterns, guidelines, food composition and diet cost

**Target level: Advanced** — execute and defend · *Prerequisites: S27* · *Part 8 · Nutrition science* · *Source: Layer 5 Nutrition Core/Working*

**Why this level.** These must be at your fingertips, and the analyses built on them — diet cost, affordability, nutrient profiling thresholds — are ones you will run yourself on national data.

**What it buys you in real life.** Threshold methodology is, as of the Supreme Court's September 2026 directions to the Centre and FSSAI, a live and unanswered empirical question inside an open policy process. That is as close as this field gets to a clear shot, and this subject is what lets you take it.

**The ladder — 3 rungs.** Complete each rung, including its build target, before starting the next.

### S29 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- The ICMR-NIN Recommended Dietary Allowances (2020) and the Dietary Guidelines for Indians (2024 revision): what they say.
- The Indian Food Composition Tables (2017) exist and have gaps.
- Regional dietary patterns and the cereal dominance of the average Indian diet.

**Skills to demonstrate**

- Look up a requirement or a food composition value correctly.
- Describe the dominant dietary pattern of your own state.

**Build target.** A written summary of the dietary pattern of your study population against ICMR requirements.

**Gate to the next rung.** You quote the RDA accurately rather than approximately.

### S29 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- Where the RDA and the 2024 guidelines are weak, and why the food composition gaps are the binding constraint on most Indian dietary analysis.
- Protein dilution of the Indian diet; rising edible oil and sugar availability; the millet policy push and its actual evidence base; the double burden within the same household.
- Dietary pattern analysis methods: a priori indices versus data-driven approaches (principal components, cluster analysis, reduced rank regression), and the problem of applying Western indices to Indian diets.
- Food security measurement: FIES, HFIAS, dietary diversity scores, and the point that food insecurity and obesity coexist because cheap energy-dense calories are the affordable option.

**Skills to demonstrate**

- Quote the ICMR RDA and the Indian dietary guidelines accurately and name their weak points.
- Derive a dietary pattern from Indian data using an appropriate method and defend the method choice.
- Measure food insecurity alongside adiposity and interpret the combination.

**Build target.** A dietary pattern analysis on Indian data using a method chosen for the question rather than by convention.

**Gate to the next rung.** You can say why a Western diet-quality index misclassifies an Indian diet, with examples.

### S29 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- Diet cost and affordability analysis using NSSO and HCES consumption data.
- Nutrient profiling models and how a front-of-pack threshold is actually derived, including the choices that are scientific and the ones that are political.
- DASH, Mediterranean, EAT-Lancet and the planetary health diet's contested applicability to India.

**Skills to demonstrate**

- Run a diet cost and affordability analysis on HCES data.
- Solve a least-cost diet optimisation meeting Indian nutrient requirements and interpret the shadow prices.
- Derive candidate India-specific nutrient profiling thresholds with sensitivity analysis over the packaged food supply.

**Build target.** An India-specific nutrient profiling threshold derivation — the question the Supreme Court has directed FSSAI to justify, with the next hearing listed for 28 September 2026.

**Gate to the next rung.** You can produce a defensible Indian threshold set and survive cross-examination on every choice in it.

---

# Part 9 · Movement, sleep and circadian biology

## S30 · Physical activity and sedentary behaviour science

**Target level: Advanced** — execute and defend · *Prerequisites: S19* · *Part 9 · Movement, sleep and circadian biology* · *Source: Layer 5 Movement Core*

**Why this level.** You will prescribe activity, evaluate activity interventions, and repeatedly correct a public message that is wrong. Advanced is the level at which you can prescribe training rather than recommend exercise.

**What it buys you in real life.** It keeps you honest in the one area where public health messaging is most comfortable and least effective, and it pairs with constrained-TDEE physiology to make a coherent, defensible public position.

**The ladder — 3 rungs.** Complete each rung, including its build target, before starting the next.

### S30 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- Aerobic and resistance training as distinct stimuli with distinct adaptations.
- The activity guidelines and what they are based on.
- That activity is weak for weight loss and strong for health — the single most important honest message in this subject.

**Skills to demonstrate**

- Give a specific activity recommendation rather than advice to be more active.
- Correct the assumption that exercise is primarily a weight intervention.

**Build target.** A written activity prescription template used with real patients.

**Gate to the next rung.** You never present exercise to a patient as the route to weight loss.

### S30 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- Exercise physiology fundamentals: VO2max and its determinants, lactate threshold, endurance and resistance adaptations, progressive overload, specificity, detraining.
- Dose-response to mortality and cardiometabolic outcomes: steep gains at the low end, flattening thereafter — so moving the least-active to slightly-active is the highest-yield population strategy.
- Sedentary behaviour as a partly independent exposure; breaks in sitting; interaction with total activity.
- The occupational physical activity paradox: high occupational activity does not confer the benefits of leisure activity and may harm — highly relevant where much manual labour is involuntary and poorly recovered.

**Skills to demonstrate**

- Write an individualised training prescription including resistance work, with progression.
- Explain the occupational paradox to a programme designer proposing a workplace steps campaign.
- Design a population activity intervention targeted at the least-active rather than the willing.

**Build target.** A delivered activity programme aimed specifically at the lowest-activity group, with uptake measured.

**Gate to the next rung.** Your programme designs target the least-active rather than the most willing.

### S30 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- Activity for weight maintenance versus for loss versus for cardiometabolic risk, held as three separate evidence bases.
- Where the public message and the honest message diverge, and how to hold the divergence in public.
- The interaction with constrained total energy expenditure: why the population weight argument fails while the health argument stands.

**Skills to demonstrate**

- Tell a health minister that an activity programme will not move prevalence and should still be funded — and make both halves land.
- Evaluate an activity intervention with the correct outcome, which is usually not weight.
- Teach activity science to clinicians and programme staff.

**Build target.** A published evaluation or position piece separating the weight and health cases for physical activity in India.

**Gate to the next rung.** Your institution's activity messaging no longer promises weight loss.

---

## S31 · Activity measurement and compositional 24-hour analysis

**Target level: Expert** — originate and adjudicate · *Prerequisites: S09, S30, S02* · *Part 9 · Movement, sleep and circadian biology* · *Source: Layer 5 Movement Core*

**Why this level.** Correct compositional analysis of the 24-hour day is still uncommon anywhere and essentially undone on Indian data. It is a methodological niche you can own within a year, it sits directly adjacent to your circadian work, and it produces novelty from datasets that already exist.

**What it buys you in real life.** It is a genuine methods claim — "recognised for a method, not just a topic" — attached to data you will already be collecting. It also makes your chrononutrition work quantitatively serious rather than questionnaire-based.

**The ladder — 4 rungs.** Complete each rung, including its build target, before starting the next.

### S31 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- An accelerometer measures acceleration, not activity, and everything else is a processing choice.
- Wear time, non-wear and epoch as the basic parameters.
- That sleep, sedentary time, light activity and MVPA sum to 1,440 minutes a day.

**Skills to demonstrate**

- Deploy an accelerometer correctly and retrieve usable data.
- Read a published accelerometry methods section and identify the cut-points used.

**Build target.** One pilot deployment of accelerometers with a written wear protocol.

**Gate to the next rung.** You can say why two studies using different cut-points are not comparable.

### S31 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- The cut-point problem and why raw-acceleration metrics such as ENMO and MAD are the modern alternative.
- Wear-time criteria, non-wear detection, device placement and their effect on the derived exposure.
- Self-report instruments and their substantial error: GPAQ and IPAQ.
- Consumer wearables and their validity, which matters because they are the only realistic route to scale in India.
- Why the 24-hour day is compositional and cannot be analysed as independent predictors.

**Skills to demonstrate**

- Process raw accelerometry in GGIR from file to exposure variable.
- Compare a self-report and an objective measure in the same sample and quantify the disagreement.
- Explain why adding an hour of activity necessarily removes an hour of something else.

**Build target.** A processed accelerometry dataset with a documented, reproducible pipeline.

**Gate to the next rung.** You can defend every processing choice in your pipeline to a reviewer.

### S31 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- Isometric log-ratio transformation and the simplex; compositional isotemporal substitution.
- How to interpret and communicate a reallocation result — the natural language for what if people slept an hour more and sat an hour less.
- Sensitivity of compositional results to zero handling and to the chosen partition.

**Skills to demonstrate**

- Conduct compositional analysis of 24-hour movement and sleep data in compositions or robCompositions, including isotemporal substitution.
- Present a reallocation result to a non-technical audience without losing the compositional constraint.
- Design a measurement protocol a district-level study can actually execute.

**Build target.** A compositional 24-hour analysis on Indian data — still uncommon anywhere and essentially undone here.

**Gate to the next rung.** Your reallocation results are interpreted correctly by the people you present them to.

### S31 · Rung 4 — Expert (originate and adjudicate)

**Concepts to understand**

- Compositional methods as a coherent framework rather than a transformation, including where they break down.
- The measurement-plus-composition combination as a methodological niche: what claims it licenses that conventional analysis cannot.
- The teaching path from cut-points to log-ratios without losing an applied audience.

**Skills to demonstrate**

- Adjudicate whether a published 24-hour analysis was done correctly.
- Teach compositional analysis to applied researchers without notes.
- Set the processing standard for a multi-site Indian study.

**Build target.** A published methods contribution on compositional 24-hour analysis in an Indian population, with code released.

**Gate to the next rung.** Another Indian group sends you their accelerometry to process, or cites your processing decisions as the reference.

---

## S32 · Sleep science and obstructive sleep apnoea

**Target level: Advanced** — execute and defend · *Prerequisites: S19* · *Part 9 · Movement, sleep and circadian biology* · *Source: Layer 5 Sleep Core*

**Why this level.** Sleep is an exposure in your own research programme and a comorbidity in your clinic. You screen and co-manage; you do not run a sleep laboratory.

**What it buys you in real life.** Sleep is the most under-measured exposure in Indian metabolic research and the easiest to add to a cohort you are already running. It is also a clinical competence that markedly improves your usefulness in a metabolic clinic.

**The ladder — 3 rungs.** Complete each rung, including its build target, before starting the next.

### S32 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- Sleep as a measurable exposure with duration, timing and quality as separable dimensions.
- Obstructive sleep apnoea as common, under-diagnosed and bidirectionally linked to obesity.
- That self-reported sleep duration is a poor measurement.

**Skills to demonstrate**

- Screen for OSA with a validated instrument.
- Ask a competent sleep history in an obesity consultation.

**Build target.** OSA screening added routinely to your obesity clinic proforma.

**Gate to the next rung.** You screen for apnoea in every patient with obesity rather than in the ones who mention snoring.

### S32 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- Sleep architecture and regulation: the two-process model, homeostatic sleep pressure and circadian timing.
- The association of short sleep with adiposity; the experimental sleep-restriction literature showing increased energy intake; and the honest caveat that the long-term causal effect on weight is smaller than the acute experiments suggest.
- OSA pathophysiology, metabolic consequences of untreated disease, and CPAP's disappointing effect on weight.
- Measurement: polysomnography, actigraphy, the Pittsburgh index, the Epworth scale, and the validity problem with self-report.
- Stress, cortisol and emotional eating; sleep restriction's effects on ghrelin, leptin and food choice.

**Skills to demonstrate**

- Refer for and interpret a sleep study.
- Choose between actigraphy and self-report for a study given a budget, and report the resulting misclassification.
- Explain to patients why treating apnoea will improve many things and probably not their weight.

**Build target.** Sleep measured objectively in one of your own studies rather than appearing as a limitation.

**Gate to the next rung.** Sleep is a measured variable in your research rather than a line in your discussion section.

### S32 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- Where the sleep-adiposity causal claim is strong and where it is inflated by short-term experiments.
- Sleep as an intervention target versus as a confounder versus as a mediator, held separately.
- Integrating sleep, activity and circadian timing as one exposure set rather than three.

**Skills to demonstrate**

- Design a study in which sleep is measured well enough to support a causal claim.
- Co-manage OSA with a sleep physician and audit the pathway.
- Teach the sleep-metabolism relationship with the caveats intact.

**Build target.** A published analysis in which objectively measured sleep is a primary exposure in an Indian sample.

**Gate to the next rung.** You can state the size of the long-term sleep effect on weight and defend the number.

---

## S33 · Circadian biology and chrononutrition

**Target level: Expert** — originate and adjudicate · *Prerequisites: S19, S21, S32* · *Part 9 · Movement, sleep and circadian biology* · *Source: Layer 5 Circadian — the candidate deep specialisation*

**Why this level.** This is the named deep specialisation: your thesis already sits here, it is under-researched in India, the exposures are cleanly measurable, and it connects biology to behaviour to environment without leaving your competence. Expert is the whole point of the map — three or four domains at this level is what a career buys.

**What it buys you in real life.** It is the ten-year programme on one coherent question that the recognition model requires: instrument validation, then prospective cohort with objective circadian and metabolic outcomes, then a randomised early-TRE trial in a group with real metabolic risk. Shift workers are the population with the clearest intervention pathway and no incumbent researcher.

**The ladder — 4 rungs.** Complete each rung, including its build target, before starting the next.

### S33 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- A circadian rhythm is endogenous, roughly 24-hourly, and entrained by external cues.
- Light is the dominant cue for the brain clock and food is the dominant cue for organ clocks.
- Chronotype and social jetlag as measurable individual characteristics.

**Skills to demonstrate**

- Administer and score MCTQ or MEQ correctly.
- Describe a person's eating window and chronotype from a diary.

**Build target.** A descriptive chronotype and eating-window profile of one study population.

**Gate to the next rung.** You can explain circadian misalignment to a lay audience in two minutes.

### S33 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- The molecular clock: CLOCK, BMAL1, PER, CRY, the transcription-translation feedback loop, and peripheral clocks in liver, adipose, muscle and pancreas.
- Entrainment: light as the dominant zeitgeber for the suprachiasmatic nucleus, feeding as the dominant zeitgeber for peripheral clocks, and internal desynchrony as the mechanistic core of chrononutrition — when the light cycle and the feeding cycle disagree, peripheral clocks decouple from the central clock.
- Diurnal variation in metabolic physiology: glucose tolerance declining across the day, higher morning insulin sensitivity, higher morning thermic effect of food, melatonin's interaction with insulin secretion.
- Chrononutrition instruments (CP-Q and variants) and their thin Indian validation status.

**Skills to demonstrate**

- Explain internal desynchrony from the molecular level to the metabolic phenotype.
- Critique a time-restricted eating study for whether timing or energy intake explains the result.
- Select an instrument appropriate to an Indian population and state what it has not been validated for.

**Build target.** A written critical review of the chrononutrition instruments available for Indian use.

**Gate to the next rung.** You can say, for any chrononutrition paper, whether it measured timing or measured intake.

### S33 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- The experimental literature in detail: forced desynchrony and circadian misalignment protocols; late-eating isocaloric crossover trials showing altered hunger, expenditure and adipose gene expression; time-restricted eating trials, where the honest reading is that most benefit is explained by reduced energy intake rather than timing per se, with early TRE having the better mechanistic case.
- Shift work and metabolic disease, which in India means a large and growing population of IT, security, transport, healthcare and manufacturing workers with essentially no occupational health protection.
- Light at night, screen exposure and urban light pollution as emerging exposures.
- Objective endpoint selection: continuous glucose monitoring, actigraphy, melatonin phase markers and what each costs.

**Skills to demonstrate**

- Validate a chrononutrition instrument in an Indian population against objective measures.
- Design, power and defend a randomised crossover trial of meal timing with objectively measured circadian and metabolic endpoints.
- Run paired CGM and actigraphy, including a properly documented N-of-1 as a teaching device.

**Build target.** A published Indian validation of a chrononutrition instrument, then a prospective cohort with objective circadian and metabolic outcomes.

**Gate to the next rung.** You can explain to a lay audience why when people eat could matter, without overclaiming that it does.

### S33 · Rung 4 — Expert (originate and adjudicate)

**Concepts to understand**

- The whole chrononutrition case as one argument from molecular clock to occupational policy, including precisely where it is weakest.
- What would falsify the timing hypothesis, and what the field would look like if it were false.
- The ten-year programme structure: instrument, cohort, trial — on one coherent question.

**Skills to demonstrate**

- Adjudicate disputes about whether timing effects are independent of energy intake.
- Lead a randomised early-TRE trial in a group with real metabolic risk, such as shift workers.
- Teach circadian biology and chrononutrition without notes, at three depths.

**Build target.** A completed randomised meal-timing trial with objective endpoints, plus the teaching module and the policy note derived from it.

**Gate to the next rung.** You are the person cited when anyone writes about meal timing in South Asian populations, and a trial you designed is running.

---

# Part 10 · Behavioural and psychological science

## S34 · Behavioural theory, choice architecture and intervention design

**Target level: Advanced** — execute and defend · *Prerequisites: S21* · *Part 10 · Behavioural and psychological science* · *Source: Layer 6 Behavioural Core*

**Why this level.** The pivot of the entire causal chain is the claim that behaviour follows the choice environment. That claim is empirical, partly contested, and you must hold it with calibrated confidence rather than as a slogan — which requires being able to design and code interventions yourself, not just cite frameworks.

**What it buys you in real life.** It is the skill that keeps you from becoming an awareness-poster researcher. Every time you are asked to design a campaign, this is what lets you say what the campaign will achieve and what would achieve more.

**The ladder — 3 rungs.** Complete each rung, including its build target, before starting the next.

### S34 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- Behaviour is shaped by context, not only by intention.
- Habit as automatic, cue-triggered behaviour rather than weak willpower.
- That information campaigns are the weakest lever and the most popular one.

**Skills to demonstrate**

- Describe a target behaviour precisely enough to measure it.
- Identify the cue, response and context in a described eating habit.

**Build target.** A written behavioural specification for one target behaviour in your own setting.

**Gate to the next rung.** You can state a target behaviour as who does what, when and where.

### S34 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- Dual-process accounts, bounded rationality, and the biases that matter for food: present bias and delay discounting, default effects, anchoring on portion, unit bias, salience, the planning-execution gap.
- Habit theory: cue-response learning, context dependence, automaticity, and why habit change requires context change — the bridge from psychology to environmental policy.
- Self-regulation and its limits, including the replication troubles around ego depletion and the shift toward self-control as situation selection.
- COM-B and the Behaviour Change Wheel; the BCT taxonomy as a coding scheme; self-determination theory; social cognitive theory; the MRC framework for complex interventions.
- Choice architecture assessed honestly: nudges work, average effects are small, and the published literature is inflated by publication bias.

**Skills to demonstrate**

- Code an intervention's active ingredients in BCT terms.
- Name the COM-B components a programme addresses and the ones it ignores.
- Read the meta-analytic exchange on nudge effect sizes and say what it shows.

**Build target.** A BCT coding of one existing Indian programme, with the gaps named.

**Gate to the next rung.** You can specify a target behaviour, its COM-B components and its BCTs for any programme put in front of you.

### S34 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- The lever hierarchy by population effect and political cost: reformulation mandates, then price instruments, then availability and marketing restriction, then front-of-pack labelling, then education campaigns, then individual counselling — the strategic heart of the whole curriculum.
- The practical conclusion: structural changes to price, availability and product composition move populations, while informational and default nudges move individuals modestly.
- Why Indian policy discussion prefers nudges precisely because they are cheap and non-confrontational.
- Digital behaviour change: app-based interventions, their modest effects and severe attrition; social norms and network interventions; financial incentive design.

**Skills to demonstrate**

- Take a vague programme idea, specify its target behaviour, name its COM-B components, code its BCTs, and state the one structural change that would outperform the whole programme.
- Design a complex intervention to the MRC framework with a falsifiable theory of change.
- Decline to run an awareness intervention and win the argument on evidence.

**Build target.** One complex intervention designed to MRC standard, with the structural alternative costed alongside it.

**Gate to the next rung.** You have successfully argued a programme away from awareness toward a structural lever.

---

## S35 · Eating behaviour, mental health and weight stigma

**Target level: Expert** — originate and adjudicate · *Prerequisites: S21, S22* · *Part 10 · Behavioural and psychological science* · *Source: Layer 6 Core; cross-cutting ethics*

**Why this level.** Weight stigma is the central ethical problem of the field and a zero-defect competency: anti-obesity work has a documented history of causing harm through stigmatising messaging, stigma independently worsens metabolic and mental health, and it is amplified by exactly the prevalence-and-risk communication public health does by default. You will be producing messages for the rest of your career, so this must be at the level where you can teach and audit others.

**What it buys you in real life.** It is the difference between a career that reduces harm and one that generates it while intending the opposite. Practically, it is also what makes patients tell you the truth about their eating, which is the precondition for every clinical measurement you take.

**The ladder — 4 rungs.** Complete each rung, including its build target, before starting the next.

### S35 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- Weight stigma exists, is common in healthcare, and harms.
- Person-first language and the specific words to avoid.
- That before-and-after imagery and prevalence-and-risk messaging can increase stigma.

**Skills to demonstrate**

- Conduct a consultation without stigmatising language.
- Identify stigmatising content in a poster or a patient leaflet.

**Build target.** A language audit of your department's obesity-related patient materials.

**Gate to the next rung.** A patient with obesity would describe your consultation as respectful without being asked.

### S35 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- Eating behaviour psychology: restraint theory and its critiques, disinhibition, the Three-Factor Eating Questionnaire and the Dutch Eating Behaviour Questionnaire, binge eating disorder, night eating syndrome.
- The clinical distinction between a disordered eating pattern and an adaptive response to restriction.
- Obesity and mental health: bidirectionality with depression, the weight effects of psychotropics, body image, disordered eating risk in adolescents.
- Stigma measurement: experienced versus internalised stigma and the validated instruments.
- Measurement invariance and item response theory at the level needed to use these scales responsibly.

**Skills to demonstrate**

- Distinguish clinically between disordered eating and an adaptive response to restriction, and change management accordingly.
- Administer and interpret a stigma or eating behaviour instrument.
- Manage a patient whose weight gain is psychotropic in origin.

**Build target.** A validated stigma or eating behaviour instrument fielded in an Indian sample.

**Gate to the next rung.** You detect disordered eating in your own clinic at a rate consistent with published prevalence.

### S35 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- The independent association of stigma with worse metabolic and mental health outcomes and with reduced care-seeking.
- The strategic point that anti-obesity messaging frequently increases stigma without changing behaviour, making message design an ethical matter rather than a tactical one.
- The serious case for weight-inclusive approaches, engaged with rather than dismissed.
- How stigma interacts with the obesity-as-disease framing in both directions.

**Skills to demonstrate**

- Test every message, poster, brief and abstract you produce for stigma, as a documented step rather than an instinct.
- Audit a colleague's consultation or a programme's materials for stigma and give usable feedback.
- Engage the weight-inclusive position on its merits in a public forum.

**Build target.** A stigma-screening step formally adopted into your institution's materials approval process.

**Gate to the next rung.** Colleagues send you their materials for a stigma check before release.

### S35 · Rung 4 — Expert (originate and adjudicate)

**Concepts to understand**

- Stigma as the central ethical problem of the field, and the discipline that follows from treating it that way.
- Where anti-obesity public health has historically caused harm, and the mechanisms by which it did.
- The teaching approach that changes clinician behaviour rather than clinician knowledge.

**Skills to demonstrate**

- Teach stigma-free practice to clinicians in a way that changes observed consultations.
- Adjudicate whether a proposed campaign is ethically deliverable.
- Set the communication standard for a national or state programme.

**Build target.** A published stigma study in an Indian population, plus a taught module that changes observed clinical behaviour.

**Gate to the next rung.** People with obesity recommend you to each other, and your department has stopped using before-and-after imagery.

---

## S36 · Qualitative and mixed methods

**Target level: Advanced** — execute and defend · *Prerequisites: none* · *Part 10 · Behavioural and psychological science* · *Source: Layer 6 Working*

**Why this level.** You will need these genuinely — for intervention co-design, implementation research, policy analysis and participatory systems mapping — and outsourcing them means outsourcing the design of your own interventions.

**What it buys you in real life.** It is the input to every implementation study, every participatory map and every adaptation of an intervention to a new district — and it is the most common missing piece in otherwise competent Indian NCD research.

**The ladder — 3 rungs.** Complete each rung, including its build target, before starting the next.

### S36 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- Qualitative research answers different questions from quantitative research rather than being weaker.
- Interview and focus group as distinct instruments with distinct dynamics.
- That a quotation is data, not decoration.

**Skills to demonstrate**

- Conduct a semi-structured interview without leading the respondent.
- Write a topic guide with open questions.

**Build target.** Five pilot interviews conducted, transcribed and read.

**Gate to the next rung.** You can run an interview in which the respondent speaks more than you do.

### S36 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- Sampling logic: purposive and theoretical sampling; saturation and its critiques.
- Thematic and framework analysis, and when each is appropriate.
- Interviewer effects in hierarchical settings, which matter acutely in Indian clinical and administrative contexts.
- COREQ reporting and what makes qualitative work credible to a quantitative reviewer.

**Skills to demonstrate**

- Build and apply a coding framework someone else could replicate.
- Run and analyse an interview study end to end.
- Report qualitative findings so that a quantitative reviewer can judge them.

**Build target.** One completed qualitative study, analysed and written to COREQ.

**Gate to the next rung.** Your coding framework survives being applied by a second coder.

### S36 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- Mixed-methods designs — convergent, explanatory sequential, exploratory sequential, embedded — chosen for a reason rather than labelled afterwards.
- Intervention co-design and participatory methods.
- The specific ethics of qualitative work on a stigmatised condition.

**Skills to demonstrate**

- Design a mixed-methods evaluation in which the qualitative component answers a question the quantitative component cannot.
- Facilitate a co-design workshop with patients or frontline workers.
- Integrate qualitative and quantitative findings rather than reporting them in parallel.

**Build target.** A mixed-methods study where integration is explicit and does analytic work.

**Gate to the next rung.** Reviewers say your qualitative chapter strengthened the paper rather than asking you to cut it.

---

# Part 11 · Food systems and commercial determinants

## S37 · Food systems, value chains and Indian food policy

**Target level: Advanced** — execute and defend · *Prerequisites: none* · *Part 11 · Food systems and commercial determinants* · *Source: Layer 6 Food systems Core*

**Why this level.** If behaviour follows the environment, whoever builds the environment is the proximate cause. Almost no Indian obesity researcher works here, which makes it the highest-differentiation layer available — and differentiation requires execution, not familiarity.

**What it buys you in real life.** It is what turns "obesity is caused by the environment" from a slogan into a supply-chain argument with named actors — which is the only version a ministry of agriculture will engage with.

**The ladder — 3 rungs.** Complete each rung, including its build target, before starting the next.

### S37 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- A food system spans production, storage, processing, distribution, retail, preparation, consumption and waste.
- Someone decides what is available, at what price, in what place.
- Indian food policy was built to end calorie deficiency, not calorie excess.

**Skills to demonstrate**

- Describe where a familiar food came from and who handled it.
- Name the main Indian food policy instruments.

**Build target.** A written supply-chain sketch of one commonly consumed packaged product.

**Gate to the next rung.** You can locate an intervention proposal somewhere in the food system rather than treating it as acting on consumers directly.

### S37 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- The HLPE food systems framework as a formal reference, learned well enough to locate any intervention within it.
- Value chains and margin structure: which actor captures value and therefore resists change; why processed food carries higher margins than fresh produce.
- Indian agricultural policy as nutrition policy: minimum support prices concentrated in rice, wheat and sugarcane; the PDS cereal orientation; sugar policy including ethanol diversion; edible oil import dependence and the palm oil mission; the millet push; horticulture's weak support.
- The nutrition transition: Popkin's stages and India's compressed, regionally uneven passage through them.

**Skills to demonstrate**

- Trace one packaged product from agricultural subsidy through sourcing, margin and marketing spend to shelf and mouth.
- Locate any proposed intervention within the HLPE framework and say which driver it acts on.
- Explain why the PDS and the obesity problem are the same policy conversation.

**Build target.** A written value-chain analysis of one Indian product category, with margins estimated.

**Gate to the next rung.** An agricultural economist finds your account of MSP and edible oil policy accurate.

### S37 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- The informal food sector, which dominates Indian street food and is invisible to most regulation.
- Trade and investment law as it constrains nutrition policy, and agricultural economics enough to read a policy paper.
- Planetary health and the diet-climate-land use link, increasingly the frame in which food policy money moves and a source of powerful allies.

**Skills to demonstrate**

- Name the three regulatory levers that would most change a product's consumption, and who would fight each one.
- Brief a policymaker on the agriculture-nutrition link with the fiscal consequences attached.
- Identify where planetary health and obesity agendas align and where they conflict.

**Build target.** A published or submitted analysis linking one Indian agricultural policy instrument to a nutrition outcome.

**Gate to the next rung.** You are invited into an agriculture policy discussion rather than a health one.

---

## S38 · Food environment measurement, retail and digital delivery

**Target level: Advanced** — execute and defend · *Prerequisites: S15, S37* · *Part 11 · Food systems and commercial determinants* · *Source: Layer 6 Core; Layer 3 spatial*

**Why this level.** India has no food environment monitoring system of any kind. Most of these methods have never been done systematically in an Indian city, each is a feasible resident project, and quick-commerce is a genuinely new exposure with essentially no Indian evidence base. This is wide-open, and it needs execution.

**What it buys you in real life.** It is the fastest route to a novel Indian dataset that nobody else holds, on an exposure that is currently changing faster than any other. It is also exactly the kind of work that gets a young researcher noticed.

**The ladder — 3 rungs.** Complete each rung, including its build target, before starting the next.

### S38 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- The food environment is the set of options available where people actually are.
- Outlet density, price and promotion as measurable properties of a place.
- That quick-commerce has put fried and sweet food fifteen minutes from most urban households.

**Skills to demonstrate**

- Walk a defined area and enumerate food outlets by type.
- Describe the digital food environment of one neighbourhood from a delivery app.

**Build target.** A pilot outlet census of one ward, with a written typology.

**Gate to the next rung.** You can describe a neighbourhood's food environment in measurable terms rather than impressions.

### S38 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- Measurement methods: outlet density and typology mapping, GIS methods, NEMS-type store and restaurant audits, school neighbourhood audits, price and availability surveys, shelf-space and promotion audits.
- Marketing: television, digital, influencer and in-app marketing; the evidence on food marketing to children; product placement and celebrity endorsement, which in India includes cricketers and film actors endorsing sugar-sweetened beverages and pan masala.
- The INFORMAS framework for benchmarking food environments.
- Retail transformation: kirana to modern trade, quick-commerce under fifteen minutes, aggregator platforms, and their combined effect on time cost and cue density.

**Skills to demonstrate**

- Audit a neighbourhood food environment with a documented, replicable method to INFORMAS-comparable standards.
- Build and clean a geocoded outlet dataset and analyse density against area deprivation.
- Design a school neighbourhood audit a resident can execute in a term.

**Build target.** A completed food environment audit of one Indian city ward, published or lodged with the municipality.

**Gate to the next rung.** Your audit method is documented well enough for another city to repeat it.

### S38 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- Digital food environment measurement, including scraping delivery platform menus and the legal and ethical constraints on doing so.
- Ten-minute household access as a genuinely new exposure with essentially no Indian evidence base.
- Linking environment measures to individual outcomes: exposure assignment, buffer choice and the resulting misclassification.

**Skills to demonstrate**

- Scrape a food delivery platform's menus for one city and turn the result into an exposure variable.
- Link a food environment measure to an individual-level outcome with a defensible exposure definition.
- Design an ongoing monitoring system rather than a one-off audit.

**Build target.** A city-scale digital food environment dataset that other researchers request.

**Gate to the next rung.** Your city's food environment dataset is the one other people ask you for.

---

## S39 · Commercial determinants and corporate political activity

**Target level: Advanced** — execute and defend · *Prerequisites: S37* · *Part 11 · Food systems and commercial determinants* · *Source: Layer 6 Core*

**Why this level.** You need to identify these strategies in live Indian examples and document them to a standard that survives a lawyer — which is execution. Expert would mean developing commercial-determinants theory, which is not where your differentiation lies.

**What it buys you in real life.** It is what lets you anticipate the opposition to any policy you propose, which is the difference between an advocacy document and a strategy. It also protects you personally: knowing the taxonomy is how you recognise an invitation for what it is.

**The ladder — 3 rungs.** Complete each rung, including its build target, before starting the next.

### S39 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- Companies act on incentives and are not neutral participants in health policy.
- The individual-responsibility frame as a deliberate strategy rather than a naive belief.
- That corporate social responsibility activity is reputational.

**Skills to demonstrate**

- Recognise the individual-responsibility frame in a public statement.
- Identify who funded a study or a conference.

**Build target.** An annotated collection of ten public statements by Indian food companies, coded by frame.

**Gate to the next rung.** You notice the frame before you notice the argument.

### S39 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- The corporate political activity taxonomy with a live Indian instance for each: framing; information and evidence; direct access and lobbying; coalition management; legal and trade strategy; market strategy.
- Market strategy in detail: reformulation to just below a regulatory threshold, portion and price-point engineering for low-income consumers, expansion into unregulated categories.
- The monitoring infrastructure: INFORMAS, the Access to Nutrition Index, the Business Impact Assessment on obesity.
- Industry funding effects as documented — they shift question selection and framing more than they corrupt analysis — and why reflexive dismissal on funding grounds is itself a failure of rigour.

**Skills to demonstrate**

- Identify each corporate political activity strategy in a live Indian example, with documentary evidence.
- Read a consultation response or a scientific panel composition and say what is being attempted.
- Judge a funded study on method rather than on funder.

**Build target.** A documented case study of corporate political activity around one live Indian regulatory process.

**Gate to the next rung.** You can predict, before a consultation closes, which three arguments industry will make and who will make them.

### S39 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- The tobacco analogy's limits: food is necessary, the industry is fragmented, and no single product is dispensable.
- How an adaptive adversary responds to each regulatory design, and what that means for evaluation.
- Personal exposure: recognising an invitation for what it is, which connects directly to the industry engagement policy in S60.

**Skills to demonstrate**

- Run an India-specific benchmarking exercise using INFORMAS or ATNI instruments.
- Anticipate the opposition to any policy you propose and design around it.
- Brief an advocacy coalition on industry strategy without becoming its spokesperson.

**Build target.** A published India benchmarking study of food industry practice — publishable and politically useful in equal measure.

**Gate to the next rung.** Your benchmarking is cited in a live Indian regulatory process.

---

# Part 12 · Economics and decision modelling

## S40 · Food demand, elasticity and the economics of externality

**Target level: Advanced** — execute and defend · *Prerequisites: S04, S29* · *Part 12 · Economics and decision modelling* · *Source: Layer 7 Economics Core*

**Why this level.** Policy arguments in India are won with fiscal numbers, not epidemiological ones. A finance ministry does not respond to prevalence; it responds to revenue, cost offset and growth. India-specific elasticities are what any tax proposal will be judged on, and estimating them is a real and doable analysis you should run yourself.

**What it buys you in real life.** It is the entry ticket to rooms epidemiologists do not enter. It also makes your tax analyses your own rather than commissioned, which matters when the policy window is short.

**The ladder — 3 rungs.** Complete each rung, including its build target, before starting the next.

### S40 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- Price affects quantity demanded, and elasticity is the measure of by how much.
- Externality as a cost borne by someone other than the buyer.
- Why finance ministries respond to revenue and cost offset rather than to prevalence.

**Skills to demonstrate**

- Interpret a published elasticity estimate.
- State the economic argument for intervening in a food market.

**Build target.** A one-page economic framing of one Indian food policy proposal.

**Gate to the next rung.** You can explain to a clinician why the health argument alone will not move a treasury.

### S40 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- Price, income and cross-price elasticity and substitution; demand system models (AIDS, QUAIDS) and their data requirements.
- Externalities and internalities: the three distinct arguments — externalised healthcare and productivity costs, internalities from present bias and imperfect information, and children who cannot consent — which license different interventions and are attacked differently.
- Consumer surplus and welfare analysis; why the standard welfare objection to food taxes is about internalities rather than externalities.
- At reading level: labour economics of obesity, with a real Indian literature gap, and behavioural public economics.

**Skills to demonstrate**

- Estimate a price elasticity for a food category from HCES or NSSO data, handling zero purchases and unit values correctly.
- Specify which of the three economic arguments a proposal rests on and defend it against the standard objection.
- Translate an elasticity into a projected consumption change and then an intake change, stating assumptions at each hop.

**Build target.** An India-specific elasticity estimate for one food category, written up for publication.

**Gate to the next rung.** An economist reviewing your estimate argues about specification rather than about competence.

### S40 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- Where elasticity estimates from household expenditure data mislead: quality substitution, unit values, and purchases as a proxy for intake.
- Heterogeneity of elasticity by income, which drives both the regressivity argument and the equity argument.
- How an elasticity becomes an input to a microsimulation and what it contributes to the final uncertainty.

**Skills to demonstrate**

- Produce elasticities disaggregated by income quintile and interpret the distributional implication.
- Defend an elasticity estimate in a policy setting against an industry-commissioned alternative.
- Feed your own elasticities into a decision model rather than borrowing foreign ones.

**Build target.** A published Indian elasticity set used as an input by someone else's policy model.

**Gate to the next rung.** Your elasticities are the ones cited in an Indian tax debate.

---

## S41 · Fiscal instruments: taxation and subsidy design in India

**Target level: Advanced** — execute and defend · *Prerequisites: S40, S37* · *Part 12 · Economics and decision modelling* · *Source: Layer 7 Economics Core*

**Why this level.** There is a live, glaring and unclaimed analytic gap here, and closing it requires you to design and evaluate tax structure yourself rather than cite others.

**What it buys you in real life.** A costed, distributionally analysed tax proposal is the single most useful document you can hand a policymaker, and India currently has nobody producing them from a nutrition-epidemiological base.

**The ladder — 3 rungs.** Complete each rung, including its build target, before starting the next.

### S41 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- A tax raises price and reduces quantity; a subsidy does the reverse.
- That India taxes carbonated and caffeinated beverages at 40 percent in the GST demerit slab from 22 September 2025, while sugar in mithai, biscuits and bakery items is taxed at 5 percent.
- That the GST Council, not the health ministry, sets these rates.

**Skills to demonstrate**

- State who controls a given tax rate in India.
- Describe the sugar tax asymmetry accurately.

**Build target.** A one-page written brief on the current Indian tax position on sugar.

**Gate to the next rung.** You can name the body that would have to act for a food tax to change.

### S41 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- Pigouvian logic; taxing the harmful attribute rather than the product; specific versus ad valorem design; tiered thresholds to induce reformulation; pass-through rates; cross-border and informal substitution.
- Regressivity handled honestly: the burden is regressive while the health benefit is progressive, and earmarking changes the net distribution.
- International evidence and design lessons: Mexico, Chile, the UK levy with its strong reformulation effect, South Africa, Philadelphia.
- Indian fiscal architecture: GST rate-setting under Article 279A, the constitutional division of taxation powers, state versus central authority over food.

**Skills to demonstrate**

- Design a tiered threshold tax on a nutrient of concern and project its reformulation incentive.
- Model pass-through and distributional incidence and present the regressivity answer with numbers rather than rhetoric.
- Explain why the UK levy produced reformulation and a volumetric tax would not have.

**Build target.** A costed tax design proposal for one Indian product category.

**Gate to the next rung.** You can answer the regressivity objection with an empirical answer that concedes what is true.

### S41 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- Subsidy reform as the mirror image: production and consumption subsidy incidence, and the political economy of removing one.
- Why any national food tax proposal must survive the GST Council, and what that implies about how a proposal should be constructed.
- Substitution across taxed and untaxed categories as the central empirical unknown in the Indian case.

**Skills to demonstrate**

- Quantify the substitution and consumption consequences of the 40 percent versus 5 percent sugar asymmetry — an obvious and unclaimed research question.
- Construct a tax proposal that could survive the GST Council, with the federal politics accounted for.
- Advise an earmarking design that makes the net distribution progressive.

**Build target.** A published analysis of the Indian sugar tax asymmetry with consumption and revenue projections.

**Gate to the next rung.** Your analysis of the asymmetry is cited in a GST Council debate.

---

## S42 · Burden of disease, economic evaluation and decision-analytic modelling

**Target level: Advanced** — execute and defend · *Prerequisites: S02, S05, S40* · *Part 12 · Economics and decision modelling* · *Source: Layer 7 Core; Layer 3 GBD*

**Why this level.** Cost per DALY averted is the currency of Indian health technology assessment, and microsimulation is the right tool for obesity. You must be able to build and defend a model, which is Advanced; you need not develop new modelling methodology.

**What it buys you in real life.** It converts your epidemiology into the only currency the treasury reads, and it is rare in India — which means the analyses you produce will be used rather than filed.

**The ladder — 3 rungs.** Complete each rung, including its build target, before starting the next.

### S42 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- DALYs and QALYs as summary measures combining length and quality of life.
- Cost-effectiveness as cost per unit of health gained, and the idea of a threshold.
- That India has a formal health technology assessment process which determines what gets funded.

**Skills to demonstrate**

- Read and interpret an ICER and a cost-effectiveness plane.
- Say what perspective and time horizon an economic evaluation used.

**Build target.** A written appraisal of one published Indian economic evaluation.

**Gate to the next rung.** You can say whether a cost-effectiveness claim used the right perspective.

### S42 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- Comparative risk assessment: population attributable fractions and their additivity problem, theoretical minimum risk exposure distributions, DALY construction, and the strong assumptions inside every GBD obesity estimate.
- Cost-of-illness methodology: prevalence versus incidence-based, direct and indirect costs, human capital versus friction cost, and the enormous uncertainty in Indian cost-of-obesity estimates, most of which are weakly constructed.
- Cost-utility analysis: perspective, time horizon, discounting, acceptability curves, and India's HTA reference case.
- Decision trees and Markov cohort models, and their limits for a chronic multifactorial condition.
- Return-on-investment analysis and the WHO Best Buys for NCDs, which is the document Indian policy actually cites.

**Skills to demonstrate**

- Build a Markov cohort model in heemod and run a probabilistic sensitivity analysis.
- Produce a defensible Indian cost-of-obesity estimate with its uncertainty stated.
- Critique a submitted economic evaluation against the Indian reference case.

**Build target.** A costed economic evaluation of one obesity intervention, to CHEERS reporting standard.

**Gate to the next rung.** Your evaluation would be accepted for consideration by the national HTA process.

### S42 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- Microsimulation as the right tool for obesity: individual-level state transitions, demographic ageing, cohort effects, heterogeneous intervention response.
- The major existing models — the UK Health Forum and PRIMEtime lineage, CHOICES, the OECD SPHeRE model — well enough to explain their structures and adapt one.
- Calibration to observed prevalence trends, validation, and reporting structural uncertainty rather than hiding it.
- Distributional and extended cost-effectiveness analysis incorporating equity and financial risk protection, which matters where catastrophic health expenditure is a central concern and is the framework in which an obesity prevention argument is strongest.
- Value-of-information analysis as the formal way to argue a specific new study is worth funding.

**Skills to demonstrate**

- Build and calibrate a microsimulation of Indian adult BMI distributions for one state, and test whether a stated prevalence target is arithmetically reachable.
- Run a sugar-sweetened beverage tax scenario through it and report incremental cost per DALY averted with proper uncertainty.
- Conduct an extended cost-effectiveness analysis reporting financial risk protection by income quintile.
- Present the result on one slide to a finance secretary.

**Build target.** A calibrated Indian state microsimulation with a published policy scenario analysis.

**Gate to the next rung.** A state health department asks you, rather than a consultancy, to cost a proposal.

---

## S43 · Health financing, HTA and pharmaceutical access in India

**Target level: Intermediate** — read, critique and commission · *Prerequisites: S42, S24* · *Part 12 · Economics and decision modelling* · *Source: Layer 7 Working*

**Why this level.** You need to navigate and critique these systems and know which door to knock on, but building health financing policy is a separate career. Intermediate is enough to commission the analysis and judge it.

**What it buys you in real life.** Access is the binding constraint on every clinical intervention in India. Knowing the financing machinery is how a treatment recommendation becomes a funded entitlement rather than an aspiration.

**The ladder — 2 rungs.** Complete each rung, including its build target, before starting the next.

### S43 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- Who pays for health care in India: out-of-pocket, PM-JAY, state schemes, private insurance.
- Catastrophic health expenditure as the central Indian financing concern.
- That coverage, not efficacy, is usually the binding constraint on a treatment reaching patients.

**Skills to demonstrate**

- Tell a patient accurately what they will and will not have to pay for.
- Say whether a given intervention is in a PM-JAY package.

**Build target.** A written coverage map for the obesity interventions you offer.

**Gate to the next rung.** You can answer who pays for any intervention you recommend.

### S43 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- PM-JAY package construction: what is and is not covered for obesity and bariatric surgery, and the process by which a package is added.
- The national HTA process and how a submission is evaluated.
- Pharmaceutical pricing economics and the National List of Essential Medicines — the mechanism by which generic semaglutide could become affordable at population scale.
- Insurance design and moral hazard as they apply to chronic weight therapy.

**Skills to demonstrate**

- Trace the route by which a specific intervention would enter a PM-JAY package or the NLEM, naming the committee and the evidence required.
- Critique a submitted HTA dossier.
- Advise a clinician or a patient group on the realistic route to coverage.

**Build target.** A written coverage-pathway analysis for one obesity intervention, shared with a professional body.

**Gate to the next rung.** You can answer who pays, and how that could change, with the mechanism named.

---

# Part 13 · Systems and complexity

## S44 · System dynamics and complexity concepts

**Target level: Advanced** — execute and defend · *Prerequisites: S02* · *Part 13 · Systems and complexity* · *Source: Layer 7 Systems Core*

**Why this level.** Obesity is the textbook complex systems problem and systems language is now compulsory in grant applications — which is exactly why to be suspicious of it. This is the layer most prone to producing beautiful diagrams that change nothing, so the only defensible level is one where you can build a running model, not draw a map.

**What it buys you in real life.** It is how you demonstrate, arithmetically, that a national target is unreachable under current policy — which is a more useful contribution than another prevalence estimate, and considerably harder to ignore.

**The ladder — 3 rungs.** Complete each rung, including its build target, before starting the next.

### S44 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- A stock is a quantity that accumulates; a flow is a rate that changes it. Body fat is a stock; obesity prevalence is a stock; diet quality is a flow.
- Feedback loops: reinforcing loops amplify, balancing loops stabilise.
- That effects can be delayed by years or decades.

**Skills to demonstrate**

- Distinguish stocks from flows in any policy argument put in front of you, out loud, in the meeting.
- Identify a reinforcing and a balancing loop in a described system.

**Build target.** A stock-flow sketch of one obesity-related policy argument you have heard.

**Gate to the next rung.** You catch a stock-flow confusion in a live discussion.

### S44 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- Causal loop and stock-and-flow diagramming to a standard from which someone else could build the model.
- Balancing and reinforcing loops identified in a real system rather than asserted, and the difference between naming a loop and demonstrating one.
- Delays as the most underrated feature of this system: twenty years from dietary change to diabetes incidence, a generation from maternal nutrition to offspring risk, years from enactment to measurable prevalence change — which guarantees political attention spans are shorter than response times and argues for process indicators.
- Nonlinearity, thresholds and tipping points; path dependence and lock-in, since once a food system is built around cheap refined carbohydrate and edible oil the cost of reversal rises with time.
- System archetypes — fixes that fail, shifting the burden, success to the successful, tragedy of the commons — and their instances in nutrition policy.
- Meadows's leverage points hierarchy used analytically: paradigms and goals beat parameters and buffers, which is why arguing about BMI cut-offs is low leverage.

**Skills to demonstrate**

- Draw a stock-and-flow diagram someone else could build from.
- Identify which archetype a failing programme is instantiating.
- Place a proposed intervention on the leverage hierarchy and say what higher-leverage alternative exists.

**Build target.** A causal loop diagram of the obesity system in one Indian district, built with the archetypes named.

**Gate to the next rung.** Every map you draw names the two loops you believe dominate and what would falsify that claim.

### S44 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- Emergence and self-organisation; attractors and multistability; adaptive adversaries — regulate one nutrient and industry reformulates toward another, which means static evaluation designs systematically overestimate durable effect.
- Resilience and robustness and their trade-off with efficiency.
- Why single-intervention evaluation underestimates whole-system intervention effects, with the UK whole-systems approach and the Amsterdam Healthy Weight Programme as reference implementations.
- Control theory applied to physiological body weight regulation, where systems language and biology genuinely meet rather than merely rhyme.

**Skills to demonstrate**

- Build and calibrate a compartmental BMI-category transition model in deSolve for an Indian state.
- Test whether a stated national or state prevalence target is arithmetically reachable — most fail, and demonstrating that is a real contribution.
- Enforce the discipline: for every map, name the dominant loops, the falsifier and the one parameter worth measuring next.

**Build target.** A calibrated BMI-transition model for one Indian state, published with the target-reachability finding.

**Gate to the next rung.** Every systems artefact you produce ends in a decision, a measurable quantity or a testable prediction.

---

## S45 · Participatory systems mapping and group model building

**Target level: Advanced** — execute and defend · *Prerequisites: S44, S36* · *Part 13 · Systems and complexity* · *Source: Layer 7 Systems Working*

**Why this level.** This is genuinely powerful in Indian district settings, it is cheap, it produces both an intervention design and a publishable output, and it cannot be delegated — facilitation is the skill.

**What it buys you in real life.** It is simultaneously a research output, an intervention design process, and the relationship-building activity that makes a district administration willing to work with you — which the document identifies as the actual precondition for implementation.

**The ladder — 3 rungs.** Complete each rung, including its build target, before starting the next.

### S45 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- A participatory map is built by stakeholders, not shown to them.
- That the senior-most person in an Indian administrative room will shape the map unless the process prevents it.
- The difference between a workshop that produces a poster and one that produces a model.

**Skills to demonstrate**

- Facilitate a small group to produce a shared causal sketch.
- Keep a dominant participant from setting the agenda.

**Build target.** A two-hour pilot mapping session with colleagues, with the map retained.

**Gate to the next rung.** A group you facilitated produces a map none of them would have drawn alone.

### S45 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- One documented protocol learned properly — STICKE or ISM — rather than a general idea of participatory mapping.
- The structured progression from stakeholder anecdote to shared causal map, and the facilitation moves that produce it.
- Group dynamics in hierarchical settings and the specific devices that flatten them.
- How to convert a participatory map into a prioritised intervention list rather than a poster.

**Skills to demonstrate**

- Run a full one-day mapping workshop to a documented protocol.
- Convert the resulting map into a prioritised intervention list with named owners.
- Handle a workshop in which the senior official disagrees with the group's map.

**Build target.** A completed district workshop with a retained map and a prioritised intervention list.

**Gate to the next rung.** Participants act on the map after the workshop ends.

### S45 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- Converting a participatory map into a parameterised, calibrated simulation.
- Publishing the method and the map as a methods contribution, not only as a local report.
- The relationship function: this process is simultaneously research, intervention design and the trust-building that makes a district administration willing to work with you.

**Skills to demonstrate**

- Run a two-day participatory mapping workshop with district health and education officials and leave with a calibrated model and three prioritised intervention points.
- Publish both the method and the map.
- Train others to facilitate the protocol.

**Build target.** A published participatory mapping study from an Indian district, with the model calibrated.

**Gate to the next rung.** A district office invites you back to run the process on a different problem.

---

## S46 · Agent-based and network modelling

**Target level: Intermediate** — read, critique and commission · *Prerequisites: S44* · *Part 13 · Systems and complexity* · *Source: Layer 7 Systems Working*

**Why this level.** Deliberately capped. ABMs are theory-generating, not effect-estimating, and the social-contagion network literature is a compulsory case study in how network causal claims fail. You need to build a simple one to understand the limits, then commission rather than specialise.

**What it buys you in real life.** Mostly the ability to say no to a fashionable method, with reasons — and to use it correctly in the narrow case where exploring saturation of an intervention effect is the actual question.

**The ladder — 2 rungs.** Complete each rung, including its build target, before starting the next.

### S46 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- An agent-based model simulates individuals and lets patterns emerge; a network is nodes and ties.
- That obesity has been claimed to spread through social networks, and that the claim is contested.
- Degree, clustering and centrality as basic network descriptors.

**Skills to demonstrate**

- Read an ABM paper and say what the agents were and what rules they followed.
- Describe a network figure correctly.

**Build target.** A run-through of an existing NetLogo or Mesa food-environment model, with parameters varied.

**Gate to the next rung.** You can say what an ABM result is and is not evidence for.

### S46 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- ABM construction: agents with income, time constraints, preferences and social influence choosing among outlets with prices and locations; using the model to explore where an intervention's effect saturates.
- The validation problem stated honestly: an ABM generates hypotheses about mechanism, it does not estimate an effect size.
- Diffusion models and dynamic transmission-style modelling for norm spread.
- The Christakis and Fowler social-contagion work and the serious methodological critiques: homophily and shared environment are not separable from contagion in observational network data.

**Skills to demonstrate**

- Build a simple food environment ABM of one ward and state its validation limits unprompted.
- Critique a published network contagion claim and name the identification problem.
- Specify to a modelling collaborator what you need and judge whether the result is interpretable.

**Build target.** A simple ward-level ABM built and documented, with an explicit statement of what it cannot establish.

**Gate to the next rung.** You can explain why an ABM result is a hypothesis and still argue that building it was worthwhile.

---

# Part 14 · Policy, law and political economy

## S47 · Policy process, framing and advocacy craft

**Target level: Advanced** — execute and defend · *Prerequisites: none* · *Part 14 · Policy, law and political economy* · *Source: Layer 8 Policy Core/Working*

**Why this level.** Vague advocacy is ignored and specific drafting is not. The ability to write a technically competent regulatory comment is rare among clinicians and immediately gets you noticed by the people who draft — which means this has to be a skill you execute, not a literature you know.

**What it buys you in real life.** It is the conversion step. Everything in the preceding thirteen parts produces knowledge; this is what turns a finding into an instrument. It is also the cheapest form of visibility available — regulatory comments are public documents with named authors.

**The ladder — 3 rungs.** Complete each rung, including its build target, before starting the next.

### S47 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- Policy is made by identifiable bodies through identifiable processes.
- Framing determines which instruments are even discussable.
- The difference between informing policy and campaigning for it.

**Skills to demonstrate**

- Identify who would have to act for a given proposal to become policy.
- Recognise the frame a public argument is operating in.

**Build target.** A written one-page note on one Indian policy proposal, naming the deciding body.

**Gate to the next rung.** You can say, for any proposal, who decides and under what authority.

### S47 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- Policy process theory used diagnostically: Kingdon's multiple streams, the advocacy coalition framework, punctuated equilibrium, and the Walt and Gilson triangle of content, context, process and actors.
- The tobacco control precedent as the closest template, including where the analogy holds and where it fails.
- The Overton window and why frame choice precedes instrument choice.
- Writing for policy audiences as a distinct genre: answer first, one page, costed recommendation, no methods section.
- The WHO and UNICEF frameworks for handling industry interference.

**Skills to demonstrate**

- Diagnose with Kingdon whether a window is open and what is missing from which stream.
- Write a four-page policy brief with the legal mechanism, evidence, quantified projected effect, counter-arguments and affected interests.
- Decide deliberately, in each instance, whether you are a researcher informing policy or an advocate campaigning — and never blur the two in one document.

**Build target.** One policy brief on an Indian instrument, circulated to a real audience.

**Gate to the next rung.** Your brief survives scrutiny by both a health secretary and an industry lawyer.

### S47 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- Regulatory drafting as a technical genre: reading actual FSSAI draft regulations and their public comments.
- Coalition assembly and working with journalists.
- Evidence-to-policy translation as a repeated process rather than a single document.

**Skills to demonstrate**

- Write a regulatory comment that a technical panel would take seriously.
- Assemble and brief a coalition around one instrument.
- Maintain a working relationship with journalists without becoming a source who overclaims.

**Build target.** A submitted regulatory comment on a live Indian draft regulation, on the public record under your name.

**Gate to the next rung.** A drafting official calls you before publishing a draft rather than after.

---

## S48 · Indian regulatory architecture and the live policy agenda

**Target level: Expert** — originate and adjudicate · *Prerequisites: S47, S37* · *Part 14 · Policy, law and political economy* · *Source: Layer 8 Policy Core*

**Why this level.** This is where the actual levers are and it is the layer Indian obesity researchers know least. Expert is justified because the standing you want is precisely "the person whose analysis the system cannot route around", and that requires knowing which body holds which power, under which statute, amendable by which process — faster and more accurately than anyone else in the room.

**What it buys you in real life.** This is the subject that converts technical competence into being consulted. It is also time-sensitive in a way nothing else in the map is: the labelling process is open now, and threshold methodology is unclaimed.

**The ladder — 4 rungs.** Complete each rung, including its build target, before starting the next.

### S48 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- FSSAI regulates food standards and labelling; the GST Council sets tax rates; the Ministry of Education and CBSE govern school food.
- That front-of-pack labelling is currently contested in India and that trans fat elimination already succeeded.
- That Article 47 places a duty on the State regarding nutrition.

**Skills to demonstrate**

- Name the regulator for a given food policy question.
- Describe the current front-of-pack labelling dispute in outline.

**Build target.** A one-page institutional map of Indian food regulation, kept current.

**Gate to the next rung.** You never have to look up which body regulates food labelling.

### S48 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- The full instrument map with statutes: food standards, labelling, claims and additives with FSSAI under the Food Safety and Standards Act 2006; misleading advertisement action with the Central Consumer Protection Authority under the Consumer Protection Act 2019; broadcast advertising content with the Ministry of Information and Broadcasting under the Cable Television Networks Rules; indirect tax with the GST Council under Article 279A; school food with the Ministry of Education, CBSE and states under PM POSHAN; NCD delivery with MoHFW and states under NP-NCD and Ayushman Arogya Mandirs; agricultural price support and PDS under the National Food Security Act 2013; and Article 47 with Article 21 as interpreted.
- Trans fat elimination as India's one clean domestic precedent for a mandatory compositional standard, and why it succeeded: a cheap technical substitute existed, so industry resistance collapsed.
- Delivery infrastructure: NP-NCD, population-based screening through Ayushman Arogya Mandirs, PM-JAY coverage.

**Skills to demonstrate**

- Name which Indian body holds which regulatory lever, under which statute, without notes.
- Explain why trans fat succeeded and why a sugar standard would be harder, from the substitute-availability argument.
- Read a draft regulation and identify its enforcement mechanism.

**Build target.** A maintained institutional and statutory brief used by your department and collaborators.

**Gate to the next rung.** Colleagues route their which-body-regulates-this questions to you.

### S48 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- The live front-of-pack battleground in detail: FSSAI's red hexagon warning-mark proposal for fat, sugar and salt, phased so products high in two or more nutrients and sweetened beverages come first; and the Supreme Court's direction of 10 September 2026 to the Centre and FSSAI to justify within ten days the threshold methodology, the hexagon choice and colour, label size and placement, the phasing rationale, and how schools will handle nutrition literacy — with the next hearing on 28 September 2026.
- The current political framing: unusual high-level attention since 2025 expressed largely through voluntary and educational measures — a call to cut edible oil use by 10 percent, reduced oil in PM POSHAN mid-day meals, sugar and oil awareness boards in CBSE schools, Eat Right India activity.
- The risk that the window closes having produced only awareness measures, which have the smallest population effect.
- At reading level: WTO and bilateral trade constraints, intellectual property and drug affordability, federal-state dynamics in health legislation.

**Skills to demonstrate**

- Brief the current state of play in five minutes to a journalist, a secretary or a committee.
- Derive India-specific nutrient profiling thresholds and defend the method — the question currently before the Court.
- Name constructively the gap between an awareness-only window and the interventions with real population effect, with evidence attached.

**Build target.** A submitted technical contribution to the live labelling process — threshold derivation, sensitivity analysis over the packaged food supply, or a formal regulatory comment.

**Gate to the next rung.** You are asked to justify a threshold rather than to comment on one.

### S48 · Rung 4 — Expert (originate and adjudicate)

**Concepts to understand**

- The Indian regulatory system as one strategic picture: which levers are movable now, which are blocked, and what would unblock each.
- How a technical question becomes a legal question and back again, as the labelling case demonstrates.
- Your own position within it: what a researcher can say that an advocate cannot, and the cost of confusing the two.

**Skills to demonstrate**

- Adjudicate a technical dispute inside a live Indian regulatory process and be accepted as the neutral expert.
- Advise both a ministry and a court-appointed process without compromising either role.
- Teach the Indian instrument map to residents and to civil society without notes.

**Build target.** A seat on a technical committee, panel or court-directed process, earned by prior technical contribution.

**Gate to the next rung.** The system cannot route around your analysis when it makes a decision in this area.

---

## S49 · Comparative and international policy

**Target level: Intermediate** — read, critique and commission · *Prerequisites: S47* · *Part 14 · Policy, law and political economy* · *Source: Layer 8 Working*

**Why this level.** Comparative analysis is useful and publishable, but it is a supporting argument rather than a differentiating capability. Read it well; do not specialise in it.

**What it buys you in real life.** Comparative work is the standard opening move in an Indian policy argument, and getting onto one international technical working group early tends to cascade into others.

**The ladder — 2 rungs.** Complete each rung, including its build target, before starting the next.

### S49 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- Other countries have tried labelling, taxes and marketing restrictions, with measured results.
- Chile, Mexico and Brazil as the standard reference cases.
- That a foreign result does not automatically transfer.

**Skills to demonstrate**

- Summarise one foreign policy package accurately.
- Say why a foreign evaluation might not apply in India.

**Build target.** A written comparison note on one instrument in two countries.

**Gate to the next rung.** You never cite a foreign policy result without naming a reason it might differ here.

### S49 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- The Chilean labelling and marketing package as the most evaluated comprehensive intervention: what was implemented, in what sequence, and what the evaluations found.
- Mexico's tax and Brazil's dietary guidelines as contrasting instruments.
- The WHO Global Action Plan and NCD targets, and how Indian commitments map to them.
- Transportability applied to policy: what has to be true for a Chilean effect to reproduce in India.
- International bodies and how technical working groups form: WHO country office and SEARO, UNICEF India, the World Obesity Federation, global NCD alliance networks.

**Skills to demonstrate**

- Write a comparative analysis of one instrument across three countries including India, with the design differences that explain outcome differences.
- Judge whether a foreign evaluation supports an Indian proposal or merely decorates it.
- Position yourself for an international technical working group, which tends to cascade.

**Build target.** A published comparative policy analysis with India as one of the cases.

**Gate to the next rung.** Your comparative section explains why the foreign result will be different here, rather than assuming it will repeat.

---

# Part 15 · Implementation and health systems delivery

## S50 · Implementation science and programme craft

**Target level: Advanced** — execute and defend · *Prerequisites: S15, S36* · *Part 15 · Implementation and health systems delivery* · *Source: Layer 8 Implementation Core*

**Why this level.** An intervention that works in a trial and fails in a district has not failed for mysterious reasons. This is the most directly employable skill in the entire map, and hybrid designs are the right shape for most Indian NCD work while still being rare here.

**What it buys you in real life.** It is what makes a district project publishable rather than merely done, and it is the skill set that makes you employable in the WHO/UNICEF/state-consultancy world regardless of what happens to your research programme.

**The ladder — 3 rungs.** Complete each rung, including its build target, before starting the next.

### S50 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- An intervention that works in a trial can fail in a district, and the reasons are specifiable.
- Fidelity: whether a programme was delivered as designed.
- The difference between a logic model and a wish list.

**Skills to demonstrate**

- Write a logic model for a familiar programme.
- Ask whether a programme was actually delivered before asking whether it worked.

**Build target.** A logic model for one existing programme in your setting, with each arrow written as a falsifiable claim.

**Gate to the next rung.** You ask about delivery before you ask about outcome.

### S50 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- The efficacy-effectiveness-implementation distinction and hybrid type 2 and 3 designs.
- Implementation outcomes as distinct from health outcomes — acceptability, adoption, appropriateness, feasibility, fidelity, cost, penetration, sustainability (Proctor's taxonomy).
- Frameworks used for their intended purpose: CFIR for determinants, RE-AIM for evaluation and reach, Normalization Process Theory for how practices embed, EPIS for phases, PRECEDE-PROCEED for planning. Pick two and know them properly.
- The ERIC taxonomy of implementation strategies, so you can name what you are doing rather than calling it capacity building.
- Indicator design across input, process, output, outcome and impact, and the trap of indicators that are easy to report rather than informative.
- Quality improvement methods: PDSA cycles, run charts, the IHI model, Kayakalp and NQAS.

**Skills to demonstrate**

- Measure implementation outcomes distinctly from health outcomes in a real evaluation.
- Run a PDSA cycle with a run chart on a live service problem in your own institution.
- Name your implementation strategies in ERIC terms in a protocol.

**Build target.** One evaluation reporting Proctor outcomes alongside health outcomes.

**Gate to the next rung.** Your evaluations report why something worked or failed with the same rigour as whether it did.

### S50 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- Fidelity versus adaptation: which components are active ingredients that must be preserved and which are adaptable periphery — the single most useful design step for anything intended to scale.
- Scale-up: the WHO and ExpandNet framework; horizontal scale versus vertical scale, and why institutionalisation in policy and budget is what lasts.
- De-implementation — stopping what does not work, which in Indian NCD programmes matters as much as starting and is politically harder.
- Process evaluation following MRC guidance; costing including the opportunity cost of frontline worker time, which most Indian programme costings simply omit.

**Skills to demonstrate**

- Specify an intervention's active ingredients versus its adaptable periphery, in writing, before piloting.
- Cost an intervention including frontline worker opportunity cost.
- Design and run a hybrid type 2 study.

**Build target.** A hybrid effectiveness-implementation study delivered in an Indian district and published with both result sets.

**Gate to the next rung.** A programme you designed has been adapted by another district without losing its active ingredients.

---

## S51 · The Indian health system and its financing mechanics

**Target level: Advanced** — execute and defend · *Prerequisites: S50* · *Part 15 · Implementation and health systems delivery* · *Source: Layer 8 Implementation Core*

**Why this level.** Any population obesity intervention in India will be delivered by ASHAs, ANMs, multipurpose workers and community health officers or not at all — so their time budget is the binding constraint on every design you make. And the state Programme Implementation Plan cycle is the mechanism by which an idea becomes a funded activity, which almost no researcher understands. You must be able to work it, not describe it.

**What it buys you in real life.** It is the difference between a recommendation and a funded activity. It is also the relationship infrastructure that makes district data available to you for research, which compounds.

**The ladder — 3 rungs.** Complete each rung, including its build target, before starting the next.

### S51 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- The service delivery ladder: sub-centre, PHC, CHC, district hospital, Ayushman Arogya Mandirs.
- The frontline cadres: ASHA, ANM, multipurpose worker, community health officer.
- That any population obesity intervention in India will be delivered by these people or not at all.

**Skills to demonstrate**

- Describe the staffing and function of each level.
- Estimate the time an ASHA actually has available.

**Build target.** A written time-budget estimate for one frontline cadre in your district.

**Gate to the next rung.** You design against a real time budget rather than an assumed one.

### S51 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- Structure and financing: National Health Mission; centrally sponsored scheme design; state health department organisation.
- The state Programme Implementation Plan cycle through which money is actually allocated — the mechanism by which an idea becomes a funded activity, which almost no researcher understands.
- Frontline workload, incentive structure and training pipeline in detail.
- Task-shifting and task-sharing evidence; non-physician-delivered NCD care; mHealth and the NCD portal with its data quality problems.
- Health information systems: HMIS, the NCD application, Ayushman Bharat Digital Mission, and the gap between what is reported and what happened.

**Skills to demonstrate**

- Read a state PIP and locate where an activity would sit.
- Design an intervention against a realistic frontline time budget, stated explicitly in the protocol.
- Audit the gap between reported and delivered service volumes in one facility.

**Build target.** A written PIP-ready activity proposal with costing and cadre time accounted for.

**Gate to the next rung.** A programme officer reads your proposal and knows immediately which budget line it belongs in.

### S51 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- Convergence: ICDS and Poshan Abhiyaan, school education, urban development, Panchayati Raj — since obesity prevention is not deliverable by the health department alone.
- Budgeting, procurement and the practical mechanics of getting an activity approved and paid for.
- The uncomfortable truth: district health administration runs on relationships, timing and the personal priorities of two or three officials. Technical excellence is necessary and nowhere near sufficient, and the researchers who get things implemented are those who have spent years being reliably useful — answering questions, producing reports on time, making officials look competent.

**Skills to demonstrate**

- Take an evidence-based obesity intervention, adapt it for a district, cost it, fit it into the NP-NCD and PIP framework, get it approved, deliver it, and publish both the effectiveness and the implementation results.
- Convene across departments at district level — a genuinely scarce skill.
- Budget real time for administrative usefulness and treat it as part of the scientific work.

**Build target.** An activity you designed appearing in a state PIP and being delivered.

**Gate to the next rung.** A district administration treats you as their researcher rather than as a visiting one.

---

# Part 16 · Computation and data

## S52 · R, reproducibility engineering and data management

**Target level: Expert** — originate and adjudicate · *Prerequisites: none* · *Part 16 · Computation and data* · *Source: Layer 9 Computation*

**Why this level.** R first and properly, then Python, and nothing else until those two are fluent. The entire epidemiological, biostatistical and evidence-synthesis toolchain lives in R; the packages for measurement error, compositional data, accelerometry, meta-analysis, Mendelian randomisation and small-area estimation have no equivalent elsewhere. Expert because this is your instrument for everything above, because you will teach it, and because reproducibility is rare in Indian academic medicine and therefore a visible quality signal.

**What it buys you in real life.** Speed and credibility simultaneously. It also makes your work auditable, which is the defence against the conclusion-first drift that the source document flags as a personal hazard.

**The ladder — 4 rungs.** Complete each rung, including its build target, before starting the next.

### S52 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- R as a language with objects, functions and packages, not a menu of commands.
- The tidyverse verbs and what a data frame is.
- That raw data is never edited and analysis is never done by hand in a spreadsheet.

**Skills to demonstrate**

- Import, clean, summarise and plot a dataset in a script that runs from top to bottom.
- Keep raw data untouched and all changes in code.

**Build target.** One dataset analysed end to end in a single script that another person can run.

**Gate to the next rung.** Your analysis reproduces from raw data with one command.

### S52 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- Writing functions rather than repeating blocks; data.table idioms for larger data.
- Git and GitHub for version control and collaboration — every project in a repo from day one.
- Quarto as a reproducible path from raw data to manuscript, and literate programming as a working style.
- SQL and DuckDB for querying large survey and hospital data.
- Field data collection tooling: REDCap, KoboToolbox or ODK.

**Skills to demonstrate**

- Write a Quarto manuscript in which every number traces to a line of code.
- Use Git properly, including branching and recovering from a mistake.
- Load a large survey into DuckDB and query it.

**Build target.** Your thesis or one full project reanalysed end to end in one Quarto document, in a public or institutional repo.

**Gate to the next rung.** Every number in your manuscript is traceable to code, and you can prove it.

### S52 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- The toolkit by competency: survival and survminer; lme4, nlme and brms; mice; dagitty; survey and WeMix; metafor; TwoSampleMR; compositions and robCompositions; GGIR; sf, spdep and INLA; simex and mecor; heemod.
- Pipeline and environment reproducibility with targets and renv.
- Stan via brms for hierarchical models.
- Simulation as a habit of thought: before running any analysis, simulate data under your assumed model and check the method recovers the truth — the single habit that prevents most analytic errors.
- On AI coding and literature tools: use them heavily and check everything, because they confidently produce wrong statistics and invented citations. Never report a number you have not reproduced yourself and never cite a paper you have not opened.
- What to skip deliberately: Julia, C++, Rust, deep learning frameworks, cloud infrastructure engineering.

**Skills to demonstrate**

- Maintain a reproducible environment a reviewer or student can run.
- Write a recovery simulation before every non-trivial analysis, as routine.
- Build a targets pipeline for a multi-step project.

**Build target.** A fully reproducible project — data, pipeline, environment, manuscript — released as a template others in your department use.

**Gate to the next rung.** Someone hands you a dataset and a question and you produce a reproducible, publication-quality analysis with figures in a single day.

### S52 · Rung 4 — Expert (originate and adjudicate)

**Concepts to understand**

- Reproducibility as an institutional practice rather than a personal habit, and how to make it the default for a group.
- Data management as asset protection: codebooks, variable dictionaries, provenance — the difference between a cohort that is an asset and one that is a mess.
- Where the R ecosystem is weak and what to do then.

**Skills to demonstrate**

- Teach R to residents to the point where they can do their own thesis analysis unaided.
- Set and enforce a data management standard for a cohort or a department.
- Review someone else's code and improve it.

**Build target.** A departmental R and reproducibility curriculum, plus a documented data management plan governing your own cohort.

**Gate to the next rung.** Residents you taught are producing reproducible analyses without you.

---

## S53 · Python for simulation, scraping and tooling

**Target level: Intermediate** — read, critique and commission · *Prerequisites: S52* · *Part 16 · Computation and data* · *Source: Layer 9 Computation*

**Why this level.** Second language, later, and deliberately capped. Python earns its place for simulation, agent-based modelling, web scraping, machine learning and software you build for other people — and for nothing else in this map. Two languages at working fluency beats six at tutorial level.

**What it buys you in real life.** Access to the digital food environment, which is currently the fastest-changing exposure in India and one that R is poorly suited to capturing.

**The ladder — 2 rungs.** Complete each rung, including its build target, before starting the next.

### S53 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- Python as a second language with a different ecosystem and different strengths.
- numpy, pandas and matplotlib as the counterparts to what you already use.
- That Python earns its place for simulation, agent-based modelling, scraping and tooling — and for nothing else here.

**Skills to demonstrate**

- Read and run someone else's Python analysis script.
- Translate a simple R analysis into Python and get the same answer.

**Build target.** One existing analysis reimplemented in Python as a learning exercise.

**Gate to the next rung.** You can read Python code in a paper's supplement without being blocked.

### S53 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- The scientific stack in practical use, and where each tool is better or worse than its R counterpart.
- Simulation and agent-based frameworks (Mesa), and when to reach for Python rather than deSolve.
- Web scraping: HTTP, HTML parsing, rate limiting, and the legal and ethical constraints on scraping a commercial platform.
- Basic software engineering hygiene — modules, tests, environments — sufficient to hand something to another person.

**Skills to demonstrate**

- Scrape a food delivery platform's menus for one city and produce a clean, documented dataset.
- Build a simple agent-based model and run scenario sweeps.
- Hand a working script to a collaborator who can run it without you.

**Build target.** A novel digital dataset acquired by your own code, documented and shared.

**Gate to the next rung.** You can acquire a digital dataset yourself rather than describing one you wish existed.

---

## S54 · India's data infrastructure, access and complex survey analysis

**Target level: Expert** — originate and adjudicate · *Prerequisites: S52, S17* · *Part 16 · Computation and data* · *Source: Layer 9 Data infrastructure*

**Why this level.** Fluency here is quietly one of the strongest forms of authority: the person who can say what the data already shows, and where it is silent, shapes what gets studied next. It is also low-cost and available immediately, which makes it the highest-return subject in the whole map during residency.

**What it buys you in real life.** Secondary analysis of public data is the cheapest high-value output available to you now, repeatedly. And a dataset you built is worth more than twenty papers on someone else's — data custody is the single highest-leverage asset in Indian academic public health, because every subsequent paper, student and collaboration flows through it.

**The ladder — 4 rungs.** Complete each rung, including its build target, before starting the next.

### S54 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- The major Indian datasets by name: NFHS, CNNS, ICMR-INDIAB, NNMS, LASI, HCES, GBD India, SRS.
- That NFHS-3 to NFHS-5 shows a 288 percent relative rise in adolescent boys against a 91 percent rise in adult women — India's obesity problem is arriving through its children.
- That survey data has weights and that ignoring them gives wrong answers.

**Skills to demonstrate**

- Download NFHS microdata and open it.
- Name which dataset would contain a given variable.

**Build target.** A weighted national prevalence estimate reproduced from NFHS microdata and checked against the published report.

**Gate to the next rung.** Your estimate matches the published figure to the decimal.

### S54 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- What each dataset can and cannot answer, including the limitation of each: NFHS cross-sectional with limited biochemistry and partial adolescent coverage; CNNS one-off; ICMR-INDIAB not powered for districts; NNMS single round; LASI older ages only; HCES household not individual and purchases not intake; GBD modelled rather than measured; SRS with weak cause certification; birth cohorts small and ageing; NCD portal and PM-JAY claims with data quality caveats; commercial retail panels expensive and opaque.
- Complex survey analysis done correctly: weights, strata, primary sampling units, and why survey or WeMix rather than unweighted regression. This is routinely got wrong in the Indian literature.
- Access mechanics: DHS Program registration, MoSPI unit-level data, institutional data use agreements.

**Skills to demonstrate**

- Analyse NFHS microdata with correct survey weights, reproducibly, in one day.
- Critique a published Indian analysis that ignored the survey design.
- Obtain a dataset through the correct formal route.

**Build target.** A published secondary analysis on Indian survey data with the design correctly handled.

**Gate to the next rung.** You can name which dataset answers any Indian obesity question in thirty seconds.

### S54 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- The practical etiquette of requesting state programme data, which is a relationship task rather than a form-filling task.
- Linking across datasets and the limits of doing so.
- The five national gaps as an opportunity list: no repeated adult anthropometric surveillance between NFHS rounds; no national cohort with objectively measured diet or physical activity; no food environment monitoring of any kind; no systematic monitoring of packaged food composition; no surveillance of GLP-1 use despite a mass generic market.

**Skills to demonstrate**

- Negotiate and execute a data use agreement, and request state programme data successfully.
- Say, for any question, which dataset answers it, which nearly does, and what would have to be collected to answer it properly.
- Design the collection that would fill one of the five gaps.

**Build target.** A funded protocol to build a dataset filling one of the five national gaps.

**Gate to the next rung.** Colleagues route their which-dataset questions to you by default.

### S54 · Rung 4 — Expert (originate and adjudicate)

**Concepts to understand**

- Data custody as the single highest-leverage asset in Indian academic public health: every subsequent paper, student and collaboration flows through it.
- The governance of a dataset you own: access policy, authorship policy, and not reproducing extractive relationships downward.
- What it takes for a dataset to outlive you.

**Skills to demonstrate**

- Build, document, govern and share a dataset others use.
- Say publicly what the Indian data does and does not show, and have that framing adopted.
- Teach Indian data infrastructure to residents without notes.

**Build target.** A cohort or surveillance dataset in the field that is yours, with a published cohort profile.

**Gate to the next rung.** One of the five national gaps is being filled by a study with your name on the protocol.

---

# Part 17 · Research craft

## S55 · Question selection and research strategy

**Target level: Expert** — originate and adjudicate · *Prerequisites: none* · *Part 17 · Research craft* · *Source: Layer 10 Research craft*

**Why this level.** Question selection is the highest-leverage decision you make and the one most researchers make by accident. Nothing else in this map compensates for getting it wrong, and the discipline it requires — declining work — is the single most important career discipline in academic medicine.

**What it buys you in real life.** It is the subject that determines whether the other sixty produce a body of work or a collection of interests. The document's own warning applies here most sharply: the map is more satisfying to hold than to walk.

**The ladder — 4 rungs.** Complete each rung, including its build target, before starting the next.

### S55 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- A research question is a choice, and most are made by accident.
- The difference between a question that is answerable and one whose answer would change something.
- That most descriptive cross-sectional studies are never cited.

**Skills to demonstrate**

- State a research question in one sentence with a population, exposure and outcome.
- Ask of a candidate question: who is waiting for this answer, and what will they do differently?

**Build target.** A written list of ten candidate questions, each scored against the who-is-waiting test.

**Gate to the next rung.** You can explain why you rejected nine of your ten candidate questions.

### S55 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- The four assets recognition is made of: a citable body of work on one named question; custody of data or a cohort; a teaching lineage; institutional position and committee membership — with the fourth manufactured by the first three.
- The portfolio ladder and what each rung costs and returns, from correspondence through secondary analysis, systematic review, instrument validation, primary cross-sectional, modelling, qualitative and policy analysis, prospective cohort, randomised trial, and guideline authorship.
- Systematic literature searching as a technical skill: database syntax across PubMed, Embase and Scopus, controlled vocabulary, search strategy documentation, citation chaining, and reference management with a real library.
- Funding sequence: intramural, then ICMR ad-hoc and task force, DST and DBT, India Alliance fellowships, ICSSR for policy-adjacent work, and international sources including Wellcome, the Gates Foundation nutrition portfolio and NIH Fogarty — each step won mostly on the last one delivered on time.

**Skills to demonstrate**

- Sequence your next three outputs so each funds the next.
- Run a documented systematic search rather than a convenience one.
- Write a grant application whose case rests on prior delivery.

**Build target.** A written three-year output plan with each item mapped to the one question and the funding rung it buys.

**Gate to the next rung.** You can name the one question you own in a single sentence.

### S55 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- Volume discipline: five well-cited papers on one question make you the person people call; twenty scattered papers make you invisible.
- Career mechanics: senior residency versus faculty entry, the DM and DNB landscape, NBEMS and recruitment norms, and the relative value of a foreign fellowship against building local data assets — where local custody generally wins, with the exception of a well-chosen postdoctoral period in a strong methods group.
- The failure modes and their early warning signs: the curriculum becoming the work, breadth without depth, a scattered portfolio, data hoarded and unpublished, advocacy capture, awareness-poster capture, administrative capture, perfectionism.
- The three stopping rules: no first-author submission in six months stops all curriculum study; any non-paper, non-dataset, non-course, non-policy side project gets ten hours; an annual scored review asking whether the one question is clearer than last year.

**Skills to demonstrate**

- Decline invitations that do not serve the one question you own, for twelve months at a time when the portfolio has scattered.
- Run the three stopping rules against your own diary and act on them.
- Choose deliberately, around 2029, between a methods postdoc and the cohort — rather than drifting into either.

**Build target.** An annual written review, scored against the competency checklist, with the previous years' scores kept.

**Gate to the next rung.** Your last five outputs all serve the question you named.

### S55 · Rung 4 — Expert (originate and adjudicate)

**Concepts to understand**

- Question selection as the discipline that determines whether the other sixty subjects produce a body of work or a collection of interests.
- The base rate of researchers who set out to transform a national health problem and did, and what that should change about strategy rather than about ambition.
- How to help someone else choose a question, which is a different and harder skill than choosing your own.

**Skills to demonstrate**

- Supervise others' question selection and improve their choices measurably.
- Say no to an attractive collaboration in public, with a reason others accept.
- Reconstruct, for any researcher's portfolio, whether it has a spine.

**Build target.** A completed decade-scale programme on one question — instrument, cohort, trial — visible as a coherent body of work.

**Gate to the next rung.** People describe your work by its question rather than by its topic.

---

## S56 · Protocol, preregistration, reporting standards and research ethics

**Target level: Advanced** — execute and defend · *Prerequisites: S55, S15* · *Part 17 · Research craft* · *Source: Layer 10 Research craft*

**Why this level.** These are the procedural defences against your own biases and the machinery that turns an idea into an approved, funded study. They must be executable to a deadline, which is Advanced.

**What it buys you in real life.** Speed with integrity. It also makes you the collaborator people want, which is how a junior researcher enters larger projects.

**The ladder — 3 rungs.** Complete each rung, including its build target, before starting the next.

### S56 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- A protocol is written before the study and states what will be done.
- Ethics committee approval and CTRI registration as prerequisites, not formalities.
- That reporting guidelines exist and are checklists for design, not for submission.

**Skills to demonstrate**

- Write a complete protocol with objectives, design, sample size, analysis and ethics.
- Take a study through an institutional ethics committee.

**Build target.** One protocol written, approved and registered.

**Gate to the next rung.** Your protocol is approved without a major revision.

### S56 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- Preregistration and protocol publication as a discipline against yourself.
- Statistical analysis plans written and dated before unblinding or before touching outcome data.
- Reporting guidelines used at the design stage: CONSORT and SPIRIT, STROBE and STROBE-nut, PRISMA, TRIPOD, CHEERS, COREQ, ISPOR-SMDM.
- Research ethics in practice: ICMR national ethical guidelines, informed consent in low-literacy settings, benefit sharing, and the specific ethics of research on stigmatised conditions — non-stigmatising language, community involvement, returning results.
- Authorship and collaboration: ICMJE criteria, CRediT, negotiating author order before the work starts, and being an excellent collaborator by delivering early and making the senior author's life easier.

**Skills to demonstrate**

- Write a SAP a statistician could execute without asking you a question.
- Preregister an analysis and then report it as preregistered, including the deviations.
- Negotiate authorship before work begins rather than after.

**Build target.** One preregistered study reported with its deviations declared.

**Gate to the next rung.** Your analyses match what you preregistered, and where they do not, you said so first.

### S56 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- Peer review as a learnable skill and an underrated accelerant: review actively and well and you read the frontier before publication and become known to editors.
- Global health ethics: extractive research relationships, the pattern where Indian data supports foreign-led analyses with Indian authors in the middle of the list, and the responsibility not to reproduce that downward with people you supervise.
- Delivery as the currency of the next grant.

**Skills to demonstrate**

- Take a vague idea to a funded, ethics-approved, preregistered protocol in eight weeks.
- Review a manuscript to a standard that improves it.
- Deliver what you promised on the date you promised it, consistently.

**Build target.** A reviewer record with a named journal, plus a protocol-to-funding cycle completed inside eight weeks.

**Gate to the next rung.** Editors invite you to review, and collaborators seek you out because you deliver.

---

# Part 18 · Teaching, communication and integrity

## S57 · Teaching, mentorship and coalition building

**Target level: Advanced** — execute and defend · *Prerequisites: none* · *Part 18 · Teaching, communication and integrity* · *Source: Layer 10 Teaching and coalitions*

**Why this level.** This is the multiplier, and it is the cheapest leverage available. A teaching lineage is one of the four assets recognition is made of, it is slow and cheap, and it is the most underrated route to standing in India. Treat it as a formal discipline rather than a natural talent.

**What it buys you in real life.** Compounding. Residents you train cite and invite you for three decades, and a module you release is read by people who will never meet you.

**The ladder — 3 rungs.** Complete each rung, including its build target, before starting the next.

### S57 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- Teaching is a skill with evidence behind it, not a talent.
- Retrieval practice and spacing work; re-reading and learning styles do not.
- That explaining something is how you find out whether you understand it.

**Skills to demonstrate**

- Run a teaching session built around retrieval rather than transmission.
- Write an assessable learning objective.

**Build target.** One taught session delivered using retrieval practice, with a written objective.

**Gate to the next rung.** Your learners can do something afterwards that they could not do before, and you measured it.

### S57 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- The learning science that holds: retrieval practice, spaced repetition, interleaving, generation effects, and cognitive load theory as the main design constraint.
- Constructive alignment — objectives, activities and assessment designed as one object — with Bloom used for writing assessable objectives rather than as decoration.
- Competency-based medical education as India has adopted it; workplace-based assessment; OSCE and mini-CEX design; feedback models.
- Explanation craft: the Feynman discipline, worked examples, analogy selection, and knowing when an analogy has started to mislead.
- Coalitions worth real investment: IAPSM and IPHA, IAPEN and the Nutrition Society of India, the obesity and endocrine societies, the Association of Physicians of India network — and civil society food policy organisations, which are few, short of technical capacity, and very receptive to a competent researcher who shows up reliably.

**Skills to demonstrate**

- Teach any subject in this map to residents without notes, within a month of studying it.
- Design an assessment that tests understanding rather than recall.
- Join one professional body and one civil society organisation and be useful to both.

**Build target.** A module on obesity taught to a resident cohort, with assessment and feedback data.

**Gate to the next rung.** Residents ask you to teach things outside your formal allocation.

### S57 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- Curriculum design at module level, so you can build a teaching unit other departments adopt — one of the most efficient reputation-building artefacts in Indian academia, because there is so little good material.
- Mentorship in both directions: two or three senior people in different domains rather than one general mentor, and deliberate training of juniors who become the network that carries your work for thirty years.
- International bodies and how technical working groups form, where getting onto one early tends to cascade.

**Skills to demonstrate**

- Design and release a teaching module other departments adopt.
- Run mentoring relationships in both directions deliberately rather than by drift.
- Build a coalition around a technical contribution rather than around a position.

**Build target.** A freely available teaching module in use at another institution, plus a named role in a professional body.

**Gate to the next rung.** A former resident invites you to speak, and another institution is teaching your module.

---

## S58 · Scientific writing, visualisation and public communication

**Target level: Advanced** — execute and defend · *Prerequisites: none* · *Part 18 · Teaching, communication and integrity* · *Source: Layer 10 Communication*

**Why this level.** Most rejected Indian manuscripts are rejected for writing and framing rather than for science, and a single good figure has more policy influence than a paper. This is an executable craft with measurable output quality.

**What it buys you in real life.** Reach per unit of work. It is also the mechanism by which competence becomes visible, and competence nobody can see does nothing.

**The ladder — 3 rungs.** Complete each rung, including its build target, before starting the next.

### S58 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- A paper is an argument, not a report of activities.
- One idea per paragraph; the sentence as the unit of clarity.
- That a figure with honest axes and a single message beats a decorated one.

**Skills to demonstrate**

- Write a paragraph that makes one point and supports it.
- Make a plot with honest axes and no decoration.

**Build target.** One manuscript section rewritten to one-idea-per-paragraph and shown to a reader.

**Gate to the next rung.** A colleague reading your draft can state your argument after one pass.

### S58 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- Scientific writing as craft: the reader-expectation approach to sentence structure, paragraph as argument, and ruthless deletion. Most rejected Indian manuscripts are rejected for writing and framing rather than for science.
- Data visualisation: appropriate marks for data shape, avoidance of decorative complexity, and making one figure that carries an argument.
- Presenting: structuring a talk around one claim, and being memorable for a specific idea rather than for a comprehensive review.
- Risk and uncertainty communication: absolute versus relative risk, natural frequencies, avoiding false precision, and correcting a claim without amplifying it.
- Writing for policy audiences as a distinct genre: answer first, one page, costed recommendation, no methods section.

**Skills to demonstrate**

- Write a paper that needs no language editing.
- Make one figure that carries an argument on its own.
- Give a talk structured around a single claim.

**Build target.** One paper accepted without language revision, and one figure reused by someone else.

**Gate to the next rung.** Reviewers comment on your science rather than on your English.

### S58 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- Public and media communication: op-eds, television interviews, the discipline of a short accurate answer, and calibrated confidence under pressure — including how to say the evidence is weak on air without becoming useless to the journalist.
- Countering misinformation, dominant in Indian diet discourse: fad diets, detox claims, influencer nutrition, and industry-adjacent messaging. Inoculation and pre-bunking rather than rebuttal, and resisting the urge to argue online.
- The four-form rule: every substantial piece of work exits as the paper, a teaching session, a one-page policy note and a plain-language explanation — roughly two extra days per paper, multiplying reach several-fold, and almost nobody does it.

**Skills to demonstrate**

- Explain the whole causal chain in ten minutes to students, three minutes to a journalist and one page to a health secretary, without contradicting yourself.
- Give a calibrated, non-amplifying correction of a viral diet claim.
- Apply the four-form rule to every substantial output.

**Build target.** One substantial piece of work released in all four forms, with reach documented.

**Gate to the next rung.** Journalists call you back, and your figures appear in other people's slides with attribution.

---

## S59 · Epistemics: philosophy of science and calibration

**Target level: Advanced** — execute and defend · *Prerequisites: none* · *Part 18 · Teaching, communication and integrity* · *Source: Cross-cutting epistemics*

**Why this level.** This is not a coda. It is the layer that determines whether thirty years of competent work points in a useful direction — and it is executable, because calibration is a trainable, scoreable skill.

**What it buys you in real life.** It is the difference between becoming an authority and becoming an advocate with credentials. It is also the only real protection against a decade of rigorous work aimed at the wrong target.

**The ladder — 3 rungs.** Complete each rung, including its build target, before starting the next.

### S59 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- Evidence varies in strength and confidence should vary with it.
- The difference between a hypothesis, a finding and a belief.
- That being wrong in public is a normal event in science and not a disgrace.

**Skills to demonstrate**

- State how confident you are in a claim, in words, and say why.
- Change a stated position when the evidence changes, out loud.

**Build target.** A written record of five current beliefs with confidence levels attached, dated.

**Gate to the next rung.** You have said the words I was wrong about that, about something you published or taught.

### S59 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- Philosophy of science enough to be useful: falsifiability and its limits, underdetermination, Kuhn on paradigms and Lakatos on research programmes, inference to the best explanation, and the Bradford Hill viewpoints understood as considerations rather than criteria.
- The mechanism-plus-difference-making view: a causal claim is best supported by both a population-level difference and a plausible mechanism — and the obesity literature is strong on mechanism and weak on population difference for almost every specific dietary factor.
- Calibration as a trainable skill: put numbers and intervals on your beliefs, write them down, score yourself later. Domain experts are usually badly calibrated because nobody scores them.
- Base rates and reference classes applied to your own plans.

**Skills to demonstrate**

- State a numerical credence for your main hypothesis, record it, and score yourself later.
- Assess a causal claim against both mechanism and population difference and say which leg is weak.
- Apply a base rate to one of your own career plans.

**Build target.** A dated calibration register of predictions with numerical credences, scored annually.

**Gate to the next rung.** Your calibration score has improved between two annual reviews.

### S59 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- Steelmanning and adversarial collaboration: construct the strongest version of a position you think is wrong — the UPF hypothesis, the carbohydrate-insulin model, weight-inclusive approaches — and design the study that would distinguish it from yours.
- The specific hazard of first-principles reasoning here: excellent at generating hypotheses and detecting a confused field, unreliable for settling empirical questions. Two failure modes — confident derivation of a false conclusion, as when thermodynamics is taken to imply that eating less is sufficient and physiological compensation turns out not to be deducible; and dismissing practices whose reasons are unrecorded, where the productive move is to find out what the practice was responding to before removing it.
- Conclusion-first drift and its procedural defence: preregistration, pre-specified predictions, and publicly recorded updates.

**Skills to demonstrate**

- Write the steelman of a position you oppose, and design the discriminating study.
- Name the three findings that would most undermine your research programme — and actually look for them.
- Notice relief when a study supports your position, and treat that as the warning sign it is.

**Build target.** A published result that contradicts a position you previously held in public.

**Gate to the next rung.** You have looked for your own disconfirming evidence and reported what you found.

---

## S60 · Ethics of obesity intervention and industry engagement

**Target level: Expert** — originate and adjudicate · *Prerequisites: S35, S39* · *Part 18 · Teaching, communication and integrity* · *Source: Cross-cutting ethics*

**Why this level.** You will be accused of nanny-statism, you will be invited by industry, and you will produce messages that can harm the people you intend to help. Each of those needs a considered position decided in advance, and you will be asked to defend them publicly — which is adjudication, not application.

**What it buys you in real life.** It is the subject that determines whether your influence, when it arrives, is trusted. It is also the one that protects you from the two most common ways this career goes wrong: capture, and harm done with good intentions.

**The ladder — 4 rungs.** Complete each rung, including its build target, before starting the next.

### S60 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- Public health interventions restrict choices and that requires justification.
- Weight stigma can be caused by well-intentioned health messaging.
- That industry will eventually invite you to something.

**Skills to demonstrate**

- State the ethical objection to a food regulation you support.
- Decline an invitation you are unsure about rather than accepting by default.

**Build target.** A first draft of a written personal policy on industry engagement, dated.

**Gate to the next rung.** You have an answer ready for an invitation before one arrives.

### S60 · Rung 2 — Intermediate (read, critique and commission)

**Concepts to understand**

- Autonomy and paternalism: the classical liberal objection to food regulation, soft and libertarian paternalism, the internality argument, and the special standing of children.
- Justice and equity: intervention-generated inequality; the progressive-benefit versus regressive-cost structure of food taxes; and the ethics of imposing dietary change on people with little discretionary income or time.
- The obesity-as-disease debate in both directions: disease framing improves access to treatment and insurance and reduces blame; it also medicalises a population condition, expands the drug market, and can displace structural action. The 2025 preclinical-clinical distinction is partly an attempt to resolve this.
- Research ethics with stigmatised conditions, and global health ethics including extractive research relationships.

**Skills to demonstrate**

- Defend a regulatory position against the autonomy objection, in public, without dismissing the objection.
- Argue the obesity-as-disease question on both sides and state where you land and why.
- Audit a proposed intervention for intervention-generated inequality.

**Build target.** A written ethical appraisal of one intervention you advocate, including the strongest objection to it.

**Gate to the next rung.** Someone who opposes your position says you represented their argument fairly.

### S60 · Rung 3 — Advanced (execute and defend)

**Concepts to understand**

- Industry engagement in operational detail: where technical collaboration is legitimate — reformulation science, supply chain data — and where it is not — funded research on your own policy questions, advisory roles that confer legitimacy.
- The necessity of a written personal policy decided before anyone invites you to anything, and the reasons it must be decided now rather than at the moment of invitation.
- The personal hazards: the empathy gap, where being personally lean and metabolically fortunate makes it easy to underestimate how much of body weight is not under voluntary control, and patients detect it instantly — your own regimen is evidence about you and nothing else; and the saviour frame, motivating as a direction and corrosive as a self-concept.

**Skills to demonstrate**

- Hold and apply a written industry policy without renegotiating it each time.
- Audit your own outputs for stigma before release, as a documented step.
- Deliberately spend time with people for whom weight management has not worked, and let it change your clinical language.

**Build target.** A dated, written industry engagement policy, plus a documented stigma-audit step in your own output process.

**Gate to the next rung.** Your industry policy has already answered an invitation before you finished reading it.

### S60 · Rung 4 — Expert (originate and adjudicate)

**Concepts to understand**

- Ethics as the layer that determines whether thirty years of competent work points somewhere useful, rather than as a compliance appendix.
- How India should adopt the preclinical-clinical categories, as an ethical question as much as a technical one.
- The standard you would want applied to the people you supervise, and the responsibility not to reproduce extraction downward.

**Skills to demonstrate**

- Adjudicate whether a proposed campaign or study is ethically deliverable, and have the judgement accepted.
- Set the ethical standard for a group or a national programme.
- Teach the ethics of obesity intervention without notes, including the arguments against your own position.

**Build target.** A published ethical contribution to the Indian obesity debate, plus an ethics standard adopted by a group you lead.

**Gate to the next rung.** You are trusted by people who disagree with you about policy.

---

## S61 · Adjacent specialist domains: recognise and route

**Target level: Introductory** — recognise and route · *Prerequisites: none* · *Part 18 · Teaching, communication and integrity* · *Source: the "literate/aware" items across all layers*

**Why this level.** These are real fields with real experts. The only competency you need is to recognise when a question has crossed into one, name the right specialist, and ask the right question. Going further is the distraction the source document warns about most explicitly.

**What it buys you in real life.** Speed and safety. The commonest failure at this boundary is not ignorance but improvisation — offering a confident answer in a field where you cannot evaluate your own reasoning.

**The ladder — 1 rung.** Complete each rung, including its build target, before starting the next.

### S61 · Rung 1 — Introductory (recognise and route)

**Concepts to understand**

- The adjacent fields and who owns each: molecular and circuit neuroscience (systems neuroscientist); molecular and cell biology including mitochondrial bioenergetics, autophagy and single-cell adipose atlases (metabolic biologist); statistical genetics beyond MR — imputation, fine-mapping, colocalisation, transcriptome-wide association, rare variant and exome work (statistical geneticist); causal discovery algorithms, which underperform on real epidemiological data (causal inference methodologist); interference and spillover in community interventions (methodologist, consulted before designing); trade and investment law including WTO constraints and intellectual property (trade lawyer); planetary health and the diet-climate-land use link (sustainability scientist); endoscopic and device therapies (bariatric endoscopist); labour economics of obesity, with a real Indian literature gap (labour economist); behavioural economics of firms and advertising research (marketing scientist); deep learning and cloud infrastructure (collaborate with someone whose job it is).
- What each field can answer that you cannot, stated as a question you would ask them.
- That the commonest failure at this boundary is not ignorance but improvisation — offering a confident answer where you cannot evaluate your own reasoning.

**Skills to demonstrate**

- Recognise, mid-conversation, that a question has left your competence, and say so.
- Name the right specialist and formulate the question so their answer is usable.
- Judge whether their answer is responsive, without being able to produce it yourself.

**Build target.** A maintained contact list of named specialists in each adjacent field, with at least three of them people you have actually worked with.

**Gate to the next rung.** You have said that is outside what I can assess, and here is who can, in public, without embarrassment.

---

---

## A closing note, taken from the source

The source document ends by warning that a map this size is more satisfying to hold than to walk, and that the version of this career that becomes nationally consequential is not the one that mastered all sixty-one subjects. It is the one that spent 2027 doing unglamorous work on a chrononutrition instrument in Raipur, published it, and then did the next thing.

The ladders are built to make that harder to avoid. Every rung ends in an artefact rather than in understanding, and every gate is a thing someone else could verify. Scored once a year against the same rungs, in writing, with the old scores kept, the document tells you whether the spike is forming. Read more often than that, it becomes the thing it is meant to prevent.
