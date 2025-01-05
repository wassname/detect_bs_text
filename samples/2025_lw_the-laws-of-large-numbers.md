---
title: The Laws of Large Numbers
date: 2025-01-04 18:06:02.387000+00:00
url: https://www.lesswrong.com/posts/EhTMM77iKBTBxBKRe/the-laws-of-large-numbers
novelty: 0.5409323783864814
score: 1.2245203256607056
baseScore: 23
voteCount: 13
---
Introduction
============

In this short post we'll discuss fine-grained variants of the law of large numbers beyond the central limit theorem. In particular we'll introduce *cumulants* as a crucial (and very nice) invariant of probability distributions to track. We'll also briefly discusses parallels with physics. This post should be interesting on its own, but the reason I'm writing it is that this story contains a central idea for (one point of view) on a certain exciting physics-inspired point of view on neural nets. While the point of view has so far been explained in somewhat [sophisticated physics language](https://arxiv.org/abs/2106.10165) (involving quantum fields and Feynman diagrams), the main points can be explained without any physics background, purely in terms of statistics. Introducing this "more elementary" view on the subject is one of the core goals of this series of posts. This first post is purely introductory, and other than "ideological" parallels, it has essentially no physics (only statistics).

Review of the central limit theorem (as a law of large numbers correction)
==========================================================================

The law of large numbers
------------------------

Most people intuitively know the *law of large numbers*: that if you take n independent measurements X1,X2,…,Xn in a random process and average them, this will converge to a specific number as n goes to infinity, namely the expectation of this process, [X].

The law of large numbers can be split up into two parts, the first of which doesn’t depend on n going to infinity. Namely:

1. *The cumulative property of means,* which itself consists of two parts:
   1. *Additivity of means.*The expectation of the sum of n random variables, [X1+⋯+Xn], is equal to the sum of their expectations: [X1]+[X2]+…+[Xn]. Here the variables don’t even have to be independent[[1]](#fn3vdew9xsk49) or drawn from the same distribution.
   2. *Linear homogeneity of means.*For any real constant λ, the expectation of the rescaled variable [λX] is equal to the rescaled expectation λ[X].
2. *Existence of exact limit of averages.*The average of n independent and identical random variables X1+⋯+Xnn has a well-defined limit, and this limit is a δ distribution (i.e., concentrates all probability at a single number).

Here a *random variable* X is a probability distribution on real numbers: the standard way of abstracting out the notion of taking a measurement in a random process. Here and later, there are some analytic conditions one should impose on the random variables, and the notion of convergence of a sequence of random variables is a slightly complicated one; we sweep these issues under the rug. Generally, a random variable can be understood as a probability function PX(r) on the reals which takes nonnegative values and integrates to 1, so: ∫∞−∞PX(r)dr=1. This encodes the familiar fact that probabilities sum to 1. Here PX measures the probability density. However, some singular limits of functions (called distributions) are allowed, and behave well with respect to the limits we will care about here so long as their tails are suitably well-behaved.

The fact that the law of large numbers follows from the two above properties is obvious, but let’s quickly spell it out. First, applying additivity and homogeneity, we see that the mean of the average of n copies of X is equal to the average of n copies of the mean [X], i.e., [X] (we’re averaging n copies of the same number). Existence of the limit means that as n goes to infinity, these averages have a deterministic limit. Since a deterministic random variable is determined by its mean, we see this limit is [X].

The central limit theorem
-------------------------

Most people reading this will also know the standard refinement of the law of large numbers, which is the *central limit theorem.*This theorem states that the average of independent variables [X1]+[X2]+…+[Xn]n drawn from the same distribution can be approximated much better than by a delta distribution, by the Gaussian distribution

σ([X],Var(X)/n): here the *variance* Var(X)≥0 is the expectation [X2] if X has mean zero, and otherwise is the expectation of the square of the mean-zero shift: \[\text{Var}(X) = [(X-[X])^2].\

Once again, the central limit theorem can be decomposed into two (new) results, the first of which, fully analogous to the cumulative property of means, holds more generally (in particular, not just in the limit):

1. *The cumulative property of variance:*
   1. *Additivity of variance.*The variance of the *sum* of n independent random variables is the sum of their variances.
   2. *Quadratic homogeneity*. Variances behave quadratically under scaling, so Var(λX)=λ2Var(X) for any real constant λ.
2. *Gaussianity of the normalized limit.*If X is a random variable with mean [X]=0, and X1,…,Xn are iid variables distributed like X, then as n goes to infinity, the sequence normalized random variables X1+…+Xn√n has a well-defined limit, and this limit is a Gaussian.

Using these items (along with the additivity of means from the previous part), we can deduce the central limit theorem. Indeed, without loss of generality we can assume that we are working with a random variable X with zero mean (since adding a constant to X results in adding the same constant to the average of n independent draws of X). The normalized sum Snormn:=X1+…+Xn√n is now a probability distribution with mean zero, and applying the two parts of the cumulative property, we see that each Sn also has variance Var(Sn)=Var(X) (the square root is there because of the *quadratic* part of homogeneity).

Thus the limit of the normalized Snormn, if it exists, must be a random variable with mean 0 and variance Var(X). Now Gaussianity tells us that the limit indeed exists and is a Gaussian. Since a Gaussian is fully determined by its mean and variance, we are done.

The third law and beyond
========================

If you’ve read the above two sections, you can probably guess where I’m going. If we think of the central limit theorem as a second-order “correction” to the law of large numbers that takes into account quadratic information about our random variable X, then there should be a “third-order” correction, which takes into account cubic information. I’m going to immediately skip from writing the law down directly to the equivalent decomposed version, which is easier to work with. The first part is a particularly straightforward extension of the “cumulative properties” that we’ve seen so far, and involves the *third cumulant*, which is κ3(X):=[(X−[X])3] (so we “adjust” X to have mean zero, then take the expectation of the cube, i.e., the third moment). Indeed, we have already seen the first and second cumulants: we have κ1(X)=[X] is the mean and κ2(X)=Var(X) is the variance.

We now have

1. *The cumulative property of the third cumulant*.
   1. *additivity.*The third cumulant behaves additively when adding together independent variables: κ3(X1+…+Xn)=κ3(X1)+…+κ3(Xn).
   2. *cubic homogeneity.*The third cumulant is homogeneous under rescaling, with κ3(λX)=λ3κ3(X).

Now what should we write for part 2? A naive guess might be that we’re now writing some kind of asymptotic formula for a different equivariant average, perhaps X1+…+Xnn1/3. But unfortunately that doesn’t work. Indeed, as before we can assume for free that X has zero mean. Now if X has nonzero second moment, then the new normalization above cannot have a limit, since we know that already when dividing by n1/2 we have a well-defined limit (a Gaussian), so if we changed normalization this would just smear it out and not give a reasonable distribution. Perhaps, then the thing to do is to assume that X has zero variance? But unfortunately here the limitations of reality make this uninteresting, as any distribution with zero variance is a deterministic delta distribution.[[2]](#fn7agzcobvmkp)

Instead, the next step in the sequence must be *perturbative*: we will not say anything new about the n→∞ limit of any normalization of the sum variable Sn=X1+⋯+Xn, but rather we will give an asymptotic *correction* to the law of large numbers at *finite* n, accurate to higher-order corrections. With this in mind, let’s write down the new limit result:

> *2. Third perturbative limit form.*Assume that our random variable X has mean zero. Then there exists a cubic polynomial P1(x)=a1+b1x+c1x2+d1x3 (independent of n) with the following property: the probability density function ψnormn(x) associated to the usual normalized sum variable Snormn=X1+…+Xn√n has the asymptotic form ψnormn(x)=σ(0,Var(X))(x)⋅(1+1√nP1(r)), up to a lower-order error term of order o(1√n), where (abusing notation) I’m writing σ(0,Var(X))(x) both for the Gaussian probability distribution and its probability density.

This is the third-order “correction” to the law of large numbers. It takes some unpacking. First, we did a bit of flipping from the Gaussian random variable σ(0,λ) to its associated probability distribution, which is always a bit of a headache. However, the way to think about this is that we just introduced a new class of probability distributions beyond Gaussians, which are Gaussians times a linear polynomial. We’re now looking for an asymptotic form of this type, where the polynomial P(r) has a constant part $P\_0$ that is independent of n and a "perturbative" part $P\_1$ that scales like 1√n. Of course as n goes to ∞, the "perturbative" term P1(x)√n goes to zero. Thus by the usual central limit theorem, we must have P0=1; otherwise we'll get the wrong n→∞ limit. Finally, note that though it is scaled by a small number, for any finite n, the polynomial P1 will eventually be negative, which technically isn’t allowed for probability distributions. It turns out that this is ok, since the place where this happens is so far away that the Gaussian tail contributes much less than the allowable order of error to the probability distribution. However this accentuates the point that being rigorous about limits and asymptotics of probability distributions is tricky and requires some analytic formalism, which as before we’ll completely rug-sweep and ignore. (The mathematicians in the audience may notice here that I am behaving like a physicist.)

Now, with all of this information in place, I claim that finding the value of P1(x)=a+bx+cx2+dx3 as an easy exercise. Indeed, there are four free real parameters, a-d, giving a four-dimensional family of possibilities for the limit. We can check that all three cumulants κ1,κ2,κ3 (i.e., the mean, variance and third cumulant) of the limit are linear functions in a-d; the cumulative property of the cumulants thus gives us three linear equations on a-d. We get a fourth linear equation from the normalization requirement ∫P1(x)σ(0,Var(X))=1. At the end of the day, we have four equations on four variables. These are solvable, and we get a formula for the first-order “cubic ⋅ Gaussian” correction. I don’t want to derive this formula here, but see the formulas on the second page of [this pdf](https://www-users.cse.umn.edu/~bobko001/papers/2022_TVP-SIAM_BU_Chebyshev-Edgeworth_With.pages.pdf) for the resulting formula (the pdf also gives a more rigorous derivation).

**Aside:**note that the first-order correction to the central limit theorem involves a cubic polynomial. On the one hand this makes sense, since we’re keeping track of up to the *third* cumulant. But on the other hand, the previous “correction”, namely the central limit theorem itself, doesn’t have a second-order polynomial scaling the Gaussian. One way to explain this is that in the perturbative formulas we’re generating, the Gaussian term already absorbs into itself any first- and second-order information: remember that we got the parameters of the Gaussian by fitting the mean and variance to be correct.

Higher cumulants and higher laws
--------------------------------

We get higher laws similarly. For each degree d, we start out with the dth cumulant, which can always be expressed in terms of the moments: κd(X)=μd(X)+polyd(μ1(X),…,μk−1(X), where “poly” denotes some fixed polynomial (independent of X) and μk(X):=[Xk] is the kth moment. Note here that flipping the formula (and iteratively expanding) lets you express the moments as polynomials of cumulants, and so cumulants and moments are two interchangeable series of “summary statistics” associated to a variable, with one or the other being better depending on context. The key property of the cumulant is as before, the “cumulative property”, i.e.,

1. *additivity*: κd(X1+…+Xn)=κd(X1)+…+κd(Xn)
2. *homogeneity*: κd(λX)=λdκd(X).

Now for the “order d” correction, we write down a general form of the correction, working with probability density functions ρX:

ρ(Snormd,x)≈ρ(σlimit)(x)⋅(1+1√nP1(x)+1nP2(x)+…). (As before, σlimit denotes the usual limit Gaussian, σ(0,Var(X)) for a mean-zero variable X.) In general, the dth correction term is the perturbative order, 1√nd−2 times a degree d polynomial in x that depends on the first through d’th cumulants of X. There is lots of pretty deep combinatorics (that I don’t know well) in the resulting formulas, involving Hermite polynomials (familiar as the natural quantum perturbations of the Harmonic oscillator in physics – this is not a coincidence!) and the [Edgeworth series](https://en.wikipedia.org/wiki/Edgeworth_series). The degree-d expansion has terms of order up to (1√n)d−2 and is correct up to an error of order (1√n)d−1 (though as before, since probability distributions can be singular, one needs to be careful when interpreting the meaning of “size of error term” rigorously).

One might hope that this will give a Taylor series for the sum distribution Snormn, which might converge even for n = 1. In fact, this is not generally the case: this expansion is fundamentally an *asymptotic* expansion (i.e., it might diverge, or converge to the wrong value, if we take the number of terms to ∞ instead of taking n to ∞). However the convergence is quite good in practice. (Note that here I was supposed to have a diagram of some examples of comparing the true sum distribution to the Edgeworth approximations; after fighting with chatgpt for an hour and not getting correctly-normalized graphs, I’m going to use my prerogative of publishing unpolished drafts.)

Multiple random variables
-------------------------

So far, we’ve been looking throughout at a single random variable X (which is a probability distribution on “one-dimensional”) values in R. When we actually apply these techniques to physics-flavored analyses of LLM’s, it will be very important that we have some fixed number (say, D) of random variables (associated to different training examples), and these are not independent.

It turns out that all of the analysis we worked out applies almost verbatim in this case. The key difference is that now we should conceptualize both the random variable X and the sum variable S=X1+…+Xn as *vector-valued,* i.e., probability distributions on RD. Once we do this, we once again have a mean value theorem (with the difference being that the variance Var(X) now is no longer a positive number, but a positive-definite DxD *matrix*). We can once again write down a normalized limiting Gaussian σlimit as the second-order approximation to our variable, and then the third- and higher-order approximations will multiply the corresponding Gaussian by polynomials of appropriate degree, now in D variables. Otherwise, the story is exactly the same. We look at cumulants, write down polynomial corrections of appropriate order, and get an expansion.

Connections to neural nets
==========================

This will be explained in much more depth in future posts, but I’ll explain very briefly the reason one might care about extending the law of large numbers for studying (realistic) neural nets. Namely, a standard entry point for physics techniques into neural nets is the “large-width” limit, where the number of neurons (corresponding to our number of independent variables in the large-number expansions above) is large. At initialization, weight parameters are uncorrelated (leading to evident iid behaviors), and as learning occurs, the relative probabilities of the parameter choices are suitably updated. Now for much of this process, it is still reasonable to model parts of the process as sums of independent random variables (this is because even during learning, a lot of what happens just consists of taking an activation, applying a function to it, rescaling it by a weight, and summing a bunch of these together in a "close enough to iid" way). Now taking only the second-order approximation -- i.e., the usual central limit theorem -- leads to modeling the neural net as a Gaussian process. This implies a certain picture of learning that is nontrivial (it can learn simple “clusterable” real-life classification problems like MNIST), but highly limited in terms of what it can learn (in some sense, it can only do clustering, and can’t use any more "interesting" geometric properties of inputs).

A priori, looking at higher perturbative terms only perturbs the resulting predictions by a small parameter. However, in some critical hyperparameter choices (that turn out to actually be preferred by efficient learning algorithms), one particular class of corrections (namely, the fourth-order ones) gets into a self-reinforcing loop and become dominant in controlling the large-scale behavior, and this leads to interesting new phenomena. This is very much not an explanation of the whole theory, but should be taken as an advertisement/appetizer for future write-ups.

Connections to physics and the stationary phase formula
=======================================================

The idea of this series of posts is to remove or defang the “physics” part of the “physics of LLM’s” ideas inherent in papers such as the beautiful [“PDLT” paper](https://arxiv.org/abs/2106.10165). However, I can’t resist quickly giving a (slightly more mathy) addendum here, that explains a direct connection between “law of large numbers” corrections and physical perturbation laws (including ones related to Feynman diagrams). This section will be more math-heavy at the end, and can be safely skipped.

The first “moral” point though can be explained without math. You see, a perennial concern of physicists (to which all of physics can sort of be reduced) is computing the so-called “Feynman path integral” of some energy functionals. This integral is in general nasty, undefined (in the sense of diverging due to various infinities) and undefinable (in the sense of the very process of Feynman integration being mathematically self-contradictory if you impose any meaningful properties), but physicists love and use it all the time.

Now just like the “sum of iid variables” example we worked out here, the way physicists approach these is in terms of a sequence of “perturbative” approximations in some parameter (called the “coupling constant” or "perturbative parameter"). To first order, physics is classical and you only care about the “deterministic” limit of the theory, which can be defined and worked with pretty nicely. The magic happens when you look at second-order behaviors (for a suitable notion of "order"). Here the physicists claim (after intoning a special ritual and sprinkling some incense, which in physics circles is what passes for rigor) that in nice cases, if you look at a suitably *quadratic* approximation of the energy function, then the Feynman integral should be a particular Gaussian (or a complex-valued analog of a Gaussian). And once they sell you this snake oil, then they say that well, a lot of interesting energy functions are *close* to being second-order, and we can therefore perturb the Gaussian to fit some higher-order behaviors. And just like in our law of large numbers example, instead of passing to some new class of functions beyond Gaussians, all higher corrections are incorporated as polynomial “corrections” times the original quadratic Gaussian approximation (known as the “free theory”).

Now though the Feynman integral formalism as used by physicists is arcane and buggy due to being very infinite-dimensional, it is based on a much more rigorously established property of certain perturbative Gaussian integrals in finite dimensions, called the “stationary phase” principle. The stationary phase principle says that, for a small perturbative parameter, certain quantum-mechanical integrals are well approximated by a formula involving higher derivatives of the energy function at its stationary points (i.e., points with zero derivative). The quantum “stationary phase” principle also has a *statistical* analog. Here one takes thermodynamic integrals instead of quantum ones, and the small "perturbative" parameter in this context is the *temperature* (rather than the coupling constant). In this case the integral is similarly dominated by terms at stationary points, with the added requirement that they be *maxima*[[3]](#fnoizjv4x73ze) rather than minima or (in higher-dimensional contexts,) saddlepoints. There is also a “mixed” form of the stationary phase formula, with separate imaginary (quantum) and real (statistical) energy components.

Now it turns out that the corrections to the central limit theorem can be precisely explained as higher-order versions of this ‘mixed’ stationary phase formula applied to the Fourier transform of the probability density functional of a random variable.

The key pair of results needed to make the connection are as follows.

Let X be a random variable with probability density function ρ(x). Let u(θ):=^ρ(θ) be the Fourier transform. Then

1. u(θ) has maximal absolute value at at u(0)=1, and unless ψ is finitely supported (i.e., X only takes finitely many values), u has no other maxima.
2. The Fourier transform of (the probability density of) the sum random variable Sn is equal to the nth *power*of the initial Fourier transform u(θ), i.e.: ^Sn=u(θ)n.

From this it follows that we can write down a new complex-valued “energy” function h(θ):=log(u(θ)), with a stationary point (with maximal real part) at h(0)=0, and then for large n, the nth sum variable has Fourier transform related to a low-temperature limit, with a temperature parameter T=1/n. Under this point of view, one can now express values of the probability density function of Sn in terms of certain temperature-1/n expectations of the energy function h, which are well-approximated (at small values of 1/n) by a stationary phase expansion. This stationary phase expansion now exactly recovers the cumulant-order expansion for the sum variable that I described in the previous section; this makes explicit the connection between the approximations we saw and similar perturbative expansions studied by physicists.

1. **[^](#fnref3vdew9xsk49)**
   
   Note that in higher-order iterations of this result, we will also assume that the variables X1,…,Xn are *independent* (thought they still won't have to be drawn from the same distribution). The fact that means are additive for non-independent variables is a very special property of means, and of means only.
2. **[^](#fnref7agzcobvmkp)**
   
   One could ask whether replacing real-valued complex variables by complex-valued ones (where [X^2] could be zero) would make this interesting. But this ends up still not working. Even if we assume that [X] = 0, the formally defined value of [X^2] no longer serves the purpose of the variance (we can still write down a law of large numbers, and its corrections -- see the later section on vector-valued random variables).
3. **[^](#fnrefoizjv4x73ze)**
   
   There are potentially confusing sign conventions here. With usual conventions, you actually take the *minimum* of the energy, but for our purposes it will be a little easier to take the convention where the *maxima* are relevant. Since the treatment in this section is entirely impressionistic and formula-free, this detail is mostly academic.
