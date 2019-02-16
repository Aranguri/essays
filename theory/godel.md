## Details of one representative Goedel Machine
### Proof techniques
Other works list all the proofs in increasing order of length and test whether they are correct or not. However, what we really care is low algorithmic complexity and not a short length. (Because a short proof can be talking about a lot of things (eg a proof full of 'for all's.)) Thus, the algorithm here will care about low algorithmic complexity. [#]


Universal TM: a TM that can simulate an arbitrary TM on an arbitrary input.

s \in S: state. It acts as the memory of the device. (It has the program p(t) and input x written)
env \in E: observations from the environment
F: S \times E \to S. ( F(s(t-1), env(t-1)) = s(t) )

x(t): input at time t
y(t): output at time t
time: it holds the time variable.

## Instructions used by proof techniques
The overall goal here is to come up with a proof that tells us that a rewiring is better than leaving the Goedel Machine as it is. We can't insert falsehoods into the proof, so it's always true.

### get-axiom(n)
initial state axioms: we specify via theorems how the storage s starts.
### apply-rule(k, m, n)
We apply the k-th inference rule in theorems indexed by m, n.
### delete-theorem(m)
### set-switchprog(m, n)
We set switchprog to s_{m:n}
### check()
It checks whether the last theorem has the following form
	u[(s(t) + (switchbit = 0), env(t))] < u[(s(t) + (switchbit = 1), env(t))]
The theorem means that the utility of the program with the new program (implied by switchbit = 1) is larger than that of the program without the change.

Even if that theorem is true, it takes time to set switchbit to 1. Thus, we run a prewired subroutine that checks whether it's possible to set switchbit to 1 before time > t. If it's not possible, we exit. (I imagine we can exit if time > t in a first instance.) We then wait for time > t. Finally, we transfer control to switchprog, which will potentially rewrite all s (except some reserved parts.)
### state2theorem(m, n)
It outputs as a theorem the value of a portion of the state. Eg
	s_{6:8}(10) = '10101'
Caveat: it takes some time to verify that the value in the state won't change. Thus, the theorem above can be started to be generated at time 5, but the machine took 5 iterations to produce it.

## Globally optimal
If the Goedel Machine proved that the utility of the program with switchbit = 1 is larger than that of the program with switchbit = 0, then it showed that rewriting itself is better than keep waiting to discover any alternative switchprog.
For the theorem above to be true, it has to take into account any meta-level of self-improvement.
We don't need to get prove the exact values of the utilities of the two programs we are comparing. Instead, we just need to say that one program is higher than the other.

## BIOPS
Inverse problem: figure out the model parameters from data observations.
Universal search: say we want to solve an inverse problem. We create some order for the programs and we run them interleaved. Say l(p) is the length of a program. And assume all programs are binary strings. On iteration i, we run all p s.t. l(p) \leq i for 2^{i - l(p)} steps. That is, at each iteration we run new programs of length l(p) = i and we run the programs we have been running for one more step.

# Terms
## Prolog
The code is composed of
* facts (eg cat(tom))
* horn clauses [eg e := a,b,c <=> (a and b and c) implies e]
* rules (eg animal(X) := cat(X))
* queries (eg ?- sibling(John, Sally))

 
