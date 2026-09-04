
"""
Formal Translation of the Empathic Logic Model into a Python Library
====================================================================

Author: Bavin Ram A R
---------------------

Affiliation: Flushtrash Planet Foundation 
-----------------------------------------

This extension of ELM presents the formal Python translation of the 
Empathic Logic Model (ELM). Because foundational psychological mechanisms 
and narrative elements function as qualitative components, specific text 
blocks and constructs containing these elements are designated with the 
tag **NOT_IMPLEMENTED**. This tag applies exclusively to the specific 
qualitative narrative sentences it references, not to the section as a 
whole. The formalized Python functions, discrete logic, and computational 
architecture are embedded directly below and between these qualitative 
placeholders. For the comprehensive qualitative framework, readers can 
reference the primary manuscript via 
Zenodo: https://doi.org/10.5281/zenodo.18614652

### Note on this Python Library Scope and Evaluation:
-----------------------------------------------------
Python Library Scope and Operational Interpretation. ELM is an applied computational 
architecture for dynamic interactive systems, evaluated through operational 
execution, transition robustness, fault tolerance, and recovery, including 
adversarial stress testing under Full-Stack Turing Deadlock, PBFT, and 
ABFT-inspired conditions, rather than abstract mathematical proofs. Its 
architecture is not intrinsically limited to human-human interaction and 
may be instantiated in human-machine interaction, machine-learning pipelines, 
AI safety, robotics, autonomous systems, and other interactive agents, subject 
to implementation and empirical validation. Artificial intelligence systems 
were utilized in the formalization and Python translation presented herein. 
Previous version of this library is available on 
Zenodo https://doi.org/10.5281/zenodo.22162082

### Future Translation Note: 
---------------------------
Its translation into engineering architectures remains open to domain-specific 
implementation, with the resulting configurations determined by the requirements 
and operational constraints of each application field and informed by subsequent 
empirical development.

### Library and Execution Note: 
-------------------------------
The resulting Python implementation may be used as an ELM computational library, 
with application-specific execution blocks constructed by implementers according 
to the requirements and operational constraints of their respective systems.

Explanation of this Library:
----------------------------
ELM governs the interpretation process by determining what the system should do 
next with received input and how that input should be handled. The input may 
originate from a sensory parser or other data parser in machine systems, or 
from biological sensory organs in human beings. By operating directly after the 
input layer of a system, ELM provides a structured mechanism for managing 
interpretation toward understanding rather than premature judgment, contextual 
data rather than static guessing, and the detection and resolution of uncertainty 
and predictive errors. This includes both preventing and resolving predictive 
errors—ELM helps identify the triggers of predictive errors and resolve them to 
prevent the errors from occurring in the first place—as well as helping to resolve 
predictive errors when others commit them.

ELM examines whether the received input contains sufficient contextual information, 
insufficient contextual information, or distorted contextual information. When 
contextual information is unavailable or distorted, ELM routes the system toward 
obtaining or refining the required contextual information through the appropriate 
contextual-extraction and interaction processes, while maintaining the safeguards 
specified by the ELM architecture to avoid introducing further predictive errors 
into the interaction.

When the input already contains sufficient contextual information, or when missing 
contextual information has been obtained through the appropriate extraction and 
refinement processes established in ELM, ELM subjects the resulting contextual 
information to the verification and stabilization processes defined by its architecture. 
When the relevant criteria are satisfied, the resulting information can then be made 
available to the system for its application-specific purpose.

ELM does not impose artificial agreement and does not seek to eliminate disagreement. 
It prioritizes proportional coherence over certainty, clarity over control, and 
understanding over judgment.

Accordingly, ELM provides an end-to-end computational routing architecture for the 
interpretation process within the operational scope defined by its formal specification, 
including contextual assessment, contextual acquisition and refinement, verification, 
stabilization, state transitions, interruption handling, and recovery. This allows 
systems such as human beings, corporations, institutions, robots, 
artificial intelligence systems, machine-learning pipelines, autonomous systems, 
and other interactive agents to operate on contextually processed and verified information 
rather than relying solely on static guessing or unverified input, subject to their 
respective implementation requirements and empirical validation.

### Version: 2.0

### License: CC BY-NC-ND 4.0 

"""



# =============================================================================
# ELM COMPUTATIONAL LIBRARY CODE BEGINS HERE. **WARNING**: The code below constitutes 
# the ELM Computational Library. Modifying the library code may alter the 
# Execution Logic of the Empathic Logic Model (ELM) Finite State Machine (FSM). 
# To execute or use this library, proceed to the bottom of this file, where the 
# headline titled "Execution and Implementation Area Begins Here" is provided. 
# Application-specific execution code, integration code, or other code intended 
# to use the ELM library should be added only below that headline.
# =============================================================================



from dataclasses import dataclass
from typing import Any, Callable, Iterable


# =============================================================================
# Section 2.1 — Interpretive Velocity Parameter (IVP) and Premature
#               Interpretive Closure (PIC)
# =============================================================================

def ivp(d_s_reaction, d_t_perception_to_stabilization):
    """Construct: Interpretive Velocity Parameter (IVP) — Section 2.1.
    Equation implemented (verbatim terms of the source formalization):
        IVP(t) := d S_reaction(t) / d t_{perception->stabilization}
    The displayed equation is the differential quotient; it is translated here
    as the quotient of the two differentials exactly as displayed.
    """
    # d_s_reaction                  -> d S_reaction(t): differential of the stabilization level of the reaction
    # d_t_perception_to_stabilization -> d t_{perception->stabilization}: differential of elapsed time from Event perception to reaction stabilization
    return d_s_reaction / d_t_perception_to_stabilization


def pic(i_avail, i_req, c_confidence, theta_confidence):
    """Construct: Premature Interpretive Closure (PIC) indicator — Section 2.1.
    Equation implemented:
        PIC(t) = 1[ I_avail(t) < I_req(t)  AND  C(t) > theta_confidence ]
    PIC(t) in {0, 1} per the source variable definitions.
    """
    # i_avail         -> I_avail(t): available contextual information at t
    # i_req           -> I_req(t): contextual information required for proportional stabilization at t
    # c_confidence    -> C(t): subjective confidence assigned to the provisional interpretation at t
    # theta_confidence -> theta_confidence: high-confidence threshold (NOT numerically specified in the source)
    return int((i_avail < i_req) and (c_confidence > theta_confidence))


def pic_sufficient_condition_implication(ivp_value, ivp_crit, i_avail, i_req, pic_value):
    """Construct: PIC sufficient-condition implication — Section 2.1.
    Equation implemented (as a material implication, i.e. the logic gate
    written with the backwards implication arrow in the source):
        PIC(t)  <==  ( IVP(t) > IVP_crit  AND  I_avail(t) < I_req(t) )
    i.e.  ( IVP(t) > IVP_crit AND I_avail(t) < I_req(t) )  =>  PIC(t).
    """
    # ivp_value  -> IVP(t)
    # ivp_crit   -> IVP_crit: velocity threshold above which the cognitive system reacts impulsively (NOT numerically specified in the source)
    # i_avail    -> I_avail(t)
    # i_req      -> I_req(t)
    # pic_value  -> PIC(t) in {0, 1}
    antecedent = (ivp_value > ivp_crit) and (i_avail < i_req)
    return (not antecedent) or (pic_value == 1)


# =============================================================================
# Section 2.4 — Interpretive Coherence and the Contextual Sufficiency
#               Criterion (formalized portions)
# =============================================================================

def a_what_why_alignment(what, why, align):
    """Construct: What-Why alignment A_What-Why — Section 2.4.
    Equation implemented:
        A_What-Why(t) := align( What(t), Why(t) ),   A_What-Why(t) in [0, 1]
    Source's own scope note: "the exact functional form of align is not
    numerically specified in the source; only the structural relationship is
    defined" — therefore `align` is injected as a callable parameter and its
    form is NOT invented here.
    """
    # what  -> What(t): subjective internal state
    # why   -> Why(t): contextual explanatory attribution
    # align -> align(., .): alignment/proportionality operator (functional form not numerically specified in the source)
    return align(what, why)


def delta_regulatory(state_forward, state_defensive):
    """Construct: regulatory-state shift Delta_regulatory — Section 2.4
    (variable definition; operationalized in Section 3.12.4).
    Equation implemented:
        Delta_regulatory(t) = state_forward(t) - state_defensive(t)
    """
    # state_forward  -> state_forward(t): forward-oriented execution state
    # state_defensive -> state_defensive(t): historical defensiveness state
    return state_forward - state_defensive


def csc(delta_reg):
    """Construct: Contextual Sufficiency Criterion (CSC) — Sections 2.4 and 3.12.4.
    Equations implemented (the source presents the same construct twice and
    composes them: Section 2.4 states "The full operational test is formalized
    in Section 3.12.4 below"):
        CSC(t) := 1[ Delta_regulatory(t) > 0 ]                        (Section 2.4)
        CSC(t) = 1[ test_stab(t) succeeds ]  with
        test_stab(t) succeeds  <=>  Delta_regulatory(t) > 0           (Section 3.12.4)
    CSC(t) in {0, 1} per the source variable definitions.
    """
    # delta_reg -> Delta_regulatory(t): observed regulatory-state shift
    return int(delta_reg > 0)


# =============================================================================
# Section 3.1 — Formal Definition (system tuple and control objective)
# =============================================================================

@dataclass
class ELMSystem:
    """Construct: ELM system tuple — Section 3.1.
    Equation implemented:
        ELM := < E, S, M, H, T, C_CSC, D >
    Field-to-symbol mapping (also given per field below):
        events              -> E:  set of Events (perceptual inputs; defined in Section 3.4)
        state_space         -> S:  state space of the interpretive system (certainty-gradient states)
        modes               -> M = {A, B, C}: three regulatory modes (Mode A Contextual Expression, Mode B Contextual Exploration, Mode C Recursive Proportional Alignment)
        handlers            -> H = {Stabilization Handler, Interruption Handler}: regulatory handlers
        transitions         -> T:  mode-transition function (defined in Sections 3.3 and 3.7)
        csc                 -> C_CSC: Contextual Sufficiency Criterion (termination condition; defined in Section 3.12.4)
        scope_directionality -> D = {intrapersonal, interpersonal} x {initiator, receiver}: dual-regulatory scope-and-directionality domain (defined in Section 3.12.2)
    """
    events: Any
    state_space: Any
    modes: Any
    handlers: Any
    transitions: Any
    csc: Any
    scope_directionality: Any


def control_objective(a_what_why_by_mode_routing, ivp_value, ivp_crit, i_avail, i_req):
    """Construct: ELM control objective — Section 3.1.
    Equation implemented:
        Objective:  max over mode routing of A_What-Why(t)
                    s.t.  IVP(t) <= IVP_crit  AND  I_avail(t) >= I_req(t)
    Returns the mode routing that attains the maximum of A_What-Why(t) among
    the supplied routings when the constraint holds.
    """
    # a_what_why_by_mode_routing -> mapping from candidate mode routings to their A_What-Why(t) values
    # ivp_value  -> IVP(t)
    # ivp_crit   -> IVP_crit (NOT numerically specified in the source)
    # i_avail    -> I_avail(t)
    # i_req      -> I_req(t)
    constraint_satisfied = (ivp_value <= ivp_crit) and (i_avail >= i_req)
    # UNSPECIFIED IN SOURCE MATH: behavior undefined for this case —
    # the source does not state what the system does when the s.t. constraint
    # is violated (the case is left unhandled; no value is returned).
    if constraint_satisfied:
        # UNSPECIFIED IN SOURCE MATH: tie-breaking among routings with equal
        # A_What-Why(t) is not defined in the source.
        return max(a_what_why_by_mode_routing, key=a_what_why_by_mode_routing.get)


# =============================================================================
# Section 3.2 — Operational Structure (formal finite-state machine)
# =============================================================================

# State labels of Q. The source defines Q ⊇ {q_A, q_B, q_C_self, q_C_shared,
# q_stab, q_int} and q_0 = q_input (Input Layer per Section 3.9).
Q_INPUT = "q_input"            # q_0: initial state on Event perception
Q_A = "q_A"                    # q_A: Mode A — Contextual Expression
Q_B = "q_B"                    # q_B: Mode B — Contextual Exploration
Q_C_SELF = "q_C_self"          # q_C,self: Mode C Self-Alignment
Q_C_SHARED = "q_C_shared"      # q_C,shared: Mode C Shared-Alignment
Q_STAB = "q_stab"              # q_stab: Stabilization Handler
Q_INT = "q_int"                # q_int: Interruption Handler
Q_CLOSURE = "q_closure"        # terminal "Closure" reached by Stab -> Closure (Section 3.7.4)

# Q: finite set of system states, Q ⊇ {q_A, q_B, q_C_self, q_C_shared, q_stab, q_int}
Q_STATES = frozenset({Q_INPUT, Q_A, Q_B, Q_C_SELF, Q_C_SHARED, Q_STAB, Q_INT, Q_CLOSURE})

# Mode labels (M = {A, B, C}).
MODE_A = "A"   # Mode A — Contextual Expression
MODE_B = "B"   # Mode B — Contextual Exploration
MODE_C = "C"   # Mode C — Recursive Proportional Alignment


@dataclass
class ContextualSignal:
    """Construct: input alphabet Sigma of the ELM-FSM — Section 3.2.
    Equation implemented:
        Sigma: input alphabet of contextual signals
               (clarity, familiarity, emotional activation, dialogue
                availability, distortion indicators)
    The Section 3.7 transition guards additionally reference the qualitative
    predicates written inside those guards; each such guard predicate is a
    component of Sigma and is mapped below. No field has a default value.
    """
    # kappa -> kappa(t): contextual-clarity level at t
    kappa: Any
    # rho -> rho(t): relational-familiarity level at t
    rho: Any
    # epsilon -> epsilon(t): emotional-activation level at t
    epsilon: Any
    # delta_dist -> delta_dist(t): interpretive-distortion level at t
    delta_dist: Any
    # iota -> iota(t): relational-instability level at t
    iota: Any
    # delta_dialog -> delta_dialog(t) in {0,1}: dialogue-availability indicator at t
    delta_dialog: Any
    # i_avail -> I_avail(t): available contextual information at t
    i_avail: Any
    # i_req -> I_req(t): contextual information required for proportional stabilization at t
    i_req: Any
    # receiver_response -> R_receiver(t): receiver-response category (used by the A -> Stabilization guard)
    receiver_response: Any
    # instability -> "without instability" flag of the A -> Stabilization guard
    instability: Any
    # requires_articulation -> "contextualized intention requires articulation" flag of the B -> A / B -> Stabilization guards
    requires_articulation: Any
    # dialog_interrupted_deferred_or_structurally_constrained -> "delta_dialog(t) interrupted, deferred, or structurally constrained" flag (B -> Interruption; Shared-Alignment -> Interruption)
    dialog_interrupted_deferred_or_structurally_constrained: Any
    # reciprocal_clarification_available -> "reciprocal clarification available" flag (Mode-C branch, Section 3.7.3)
    reciprocal_clarification_available: Any
    # refinement_remains_insufficient -> "refinement remains insufficient" flag (Self-Alignment -> Shared-Alignment or B)
    refinement_remains_insufficient: Any
    # delta_reg -> Delta_regulatory(t): observed regulatory-state shift (Stabilization Handler)
    delta_reg: Any
    # requires_incremental_articulation -> "Requires(incremental articulation)" flag (Stabilization self-loop guard)
    requires_incremental_articulation: Any
    # constitutes_reentry_into_prior_modes -> negated re-entry clause of the Stabilization self-loop guard
    constitutes_reentry_into_prior_modes: Any


@dataclass
class ELMFSM:
    """Construct: ELM-FSM — Section 3.2.
    Equation implemented:
        ELM-FSM = ( Q, Sigma, delta, q_0, F )
    Field-to-symbol mapping:
        q      -> Q: finite set of system states (Q_STATES; Q ⊇ {q_A, q_B, q_C_self, q_C_shared, q_stab, q_int})
        sigma  -> Sigma: input alphabet of contextual signals (ContextualSignal)
        delta  -> delta: Q x Sigma -> Q state-transition function (defined by Section 3.3 mode-selection logic and Section 3.7 external transitions)
        q0     -> q_0 = q_input: initial state on Event perception
        f      -> F = {q_stab | CSC satisfied}: accepting/terminal states
    """
    q: Any
    sigma: Any
    delta: Any
    q0: Any
    f: Any


# =============================================================================
# Section 3.3 — Mode Selection Logic
# =============================================================================

def mode_selection(kappa, kappa_star, rho, rho_star, epsilon, epsilon_star,
                   delta_dist, delta_dist_star, iota, iota_star, delta_dialog):
    """Construct: Mode Selection Logic — Section 3.3.
    Equation implemented (piecewise, rows checked in the source's listed order):
        Mode(t) = A  if  kappa(t) >= kappa*  AND  rho(t) >= rho*  AND  delta_dialog(t) = 1
        Mode(t) = B  if  ( kappa(t) < kappa*  OR  rho(t) < rho*
                           OR  ( kappa(t) < kappa*  AND  rho(t) < rho* ) )
                       AND  delta_dialog(t) = 1
        Mode(t) = C  if  epsilon(t) > epsilon*  OR  delta_dist(t) > delta_dist*
                       OR  iota(t) > iota*  OR  delta_dialog(t) = 0
    The third disjunct of the Mode-B row is logically redundant but is written
    in the source; it is preserved verbatim (no cleanup, per translation rules).
    """
    # kappa         -> kappa(t): contextual-clarity level at t
    # kappa_star    -> kappa*: "sufficient" clarity threshold (NOT numerically specified in the source)
    # rho           -> rho(t): relational-familiarity level at t
    # rho_star      -> rho*: "sufficient" familiarity threshold (NOT numerically specified in the source)
    # epsilon       -> epsilon(t): emotional-activation level at t
    # epsilon_star  -> epsilon*: "sufficient" activation threshold (NOT numerically specified in the source)
    # delta_dist    -> delta_dist(t): interpretive-distortion level at t
    # delta_dist_star -> delta_dist*: distortion threshold (NOT numerically specified in the source)
    # iota          -> iota(t): relational-instability level at t
    # iota_star     -> iota*: instability threshold (NOT numerically specified in the source)
    # delta_dialog  -> delta_dialog(t) in {0,1}: dialogue-availability indicator at t
    if (kappa >= kappa_star) and (rho >= rho_star) and (delta_dialog == 1):
        return MODE_A
    elif (((kappa < kappa_star) or (rho < rho_star) or ((kappa < kappa_star) and (rho < rho_star)))
          and (delta_dialog == 1)):
        return MODE_B
    elif ((epsilon > epsilon_star) or (delta_dist > delta_dist_star)
          or (iota > iota_star) or (delta_dialog == 0)):
        return MODE_C
    # UNSPECIFIED IN SOURCE MATH: behavior undefined for this case —
    # no piecewise row matches (the written rows cover the signal space, but
    # no explicit fallthrough is defined; the case is left unhandled).
    return None


def a_to_c_guard(epsilon, epsilon_star, delta_dist, delta_dist_star, iota, iota_star):
    """Construct: Modes A and B -> Mode C transition guard — Section 3.3
    (A -> C row; the identical formula is written separately for B -> C).
    Equation implemented:
        A -> C:  epsilon(t) > epsilon*  OR  delta_dist(t) > delta_dist*  OR  iota(t) > iota*
    """
    # epsilon        -> epsilon(t)
    # epsilon_star   -> epsilon*
    # delta_dist     -> delta_dist(t)
    # delta_dist_star -> delta_dist*
    # iota           -> iota(t)
    # iota_star      -> iota*
    return (epsilon > epsilon_star) or (delta_dist > delta_dist_star) or (iota > iota_star)


def b_to_c_guard(epsilon, epsilon_star, delta_dist, delta_dist_star, iota, iota_star):
    """Construct: Modes A and B -> Mode C transition guard — Section 3.3
    (B -> C row; written separately from the A -> C row in the source, so it
    is implemented as a separate function — no merging).
    Equation implemented:
        B -> C:  epsilon(t) > epsilon*  OR  delta_dist(t) > delta_dist*  OR  iota(t) > iota*
    """
    # epsilon        -> epsilon(t)
    # epsilon_star   -> epsilon*
    # delta_dist     -> delta_dist(t)
    # delta_dist_star -> delta_dist*
    # iota           -> iota(t)
    # iota_star      -> iota*
    return (epsilon > epsilon_star) or (delta_dist > delta_dist_star) or (iota > iota_star)


def mode_c_subform(delta_dialog):
    """Construct: Mode C duality (Mode-C-subform) — Section 3.3.
    Equation implemented:
        Mode-C-subform(t) = Shared-Alignment  if delta_dialog(t) = 1
                            Self-Alignment    if delta_dialog(t) = 0
    """
    # delta_dialog -> delta_dialog(t) in {0,1}
    if delta_dialog == 1:
        return "Shared-Alignment"
    if delta_dialog == 0:
        return "Self-Alignment"
    # UNSPECIFIED IN SOURCE MATH: behavior undefined for this case —
    # delta_dialog(t) outside {0, 1} is not defined in the source.
    return None


# =============================================================================
# Section 3.4 — Definition of Event
# =============================================================================

# Construct: Event universe E — Section 3.4.
# Equation implemented:
#     E := {behavior} U {spoken or written message} U {silence or absence of
#          response} U {environmental change} U {relational cue}
EVENT_UNIVERSE = frozenset({
    "behavior",
    "spoken or written message",
    "silence or absence of response",
    "environmental change",
    "relational cue",
})


def event_triggers_initial_ivp(e, t_onset):
    """Construct: Event triggering relation — Section 3.4.
    Equation implemented:
        e  ->  IVP(t_0),   t_0 = Event onset
    The relation is returned as the triple (Event, triggered construct, onset
    time). The source distinguishes Event from Interpretive What: "An Event is
    not yet an interpretation."
    """
    # e        -> e: an Event instance (e in E)
    # t_onset  -> t_0: Event onset
    # UNSPECIFIED IN SOURCE MATH: behavior undefined for this case —
    # the magnitude of IVP(t_0) as a function of e is not specified.
    return (e, "IVP", t_onset)


# =============================================================================
# Section 3.5 — Operational Definitions of What and Why
# =============================================================================

def what_binding(mode):
    """Construct: mode-dependent What typing (binding) — Section 3.5.
    Equation implemented:
        What(t) : Mode(t) -> {Intended, Observed, Interpretive}
        What(t) = Intended What                 if Mode(t) = A
                  Observed What                 if Mode(t) = B
                  Observed or Interpretive What if Mode(t) = C
    Mode C binds the disjunction "Observed or Interpretive What"; it is
    returned as the pair of admissible types.
    """
    # mode -> Mode(t) in {A, B, C}
    if mode == MODE_A:
        return ("Intended",)
    if mode == MODE_B:
        return ("Observed",)
    if mode == MODE_C:
        return ("Observed", "Interpretive")
    # UNSPECIFIED IN SOURCE MATH: behavior undefined for this case —
    # What(t) is typed only over Mode(t) in {A, B, C}.
    return None


# Construct: Operational What — Section 3.5.
# Equation implemented:
#     Operational What(t) := U_{m in {A,B,C}} What_m(t)
OPERATIONAL_WHAT = frozenset({"Intended", "Observed", "Interpretive"})


# =============================================================================
# Section 3.6 — Recognition of Missing Context
# =============================================================================

def rmc(i_avail, i_req):
    """Construct: Recognition of Missing Context (RMC) — Section 3.6.
    Equation implemented:
        RMC(t) := 1[ I_avail(t) < I_req(t) ]
    RMC(t) in {0, 1} per the source variable definitions. The source describes
    RMC as "the primary cognitive decelerator that interrupts rapid affective
    stabilization".
    """
    # i_avail -> I_avail(t): available contextual information at t
    # i_req   -> I_req(t): contextual information required for proportional stabilization at t
    return int(i_avail < i_req)


def rmc_consequence(rmc_value, d_ivp_dt, generate_provisional_attribution,
                    initiate_contextual_clarification):
    """Construct: RMC consequence (logic gate) — Section 3.6.
    Equation implemented (material implication):
        RMC(t) = 1  =>  d IVP/dt <= 0
                      AND ( Generate provisional contextual attribution
                            OR Initiate contextual clarification )
    "d IVP/dt <= 0" encodes "decelerate Interpretive Velocity" per the source.
    """
    # rmc_value                             -> RMC(t) in {0, 1}
    # d_ivp_dt                              -> d IVP/dt
    # generate_provisional_attribution      -> "Generate provisional contextual attribution" disjunct
    # initiate_contextual_clarification     -> "Initiate contextual clarification" disjunct
    antecedent = (rmc_value == 1)
    consequent = (d_ivp_dt <= 0) and (generate_provisional_attribution or initiate_contextual_clarification)
    return (not antecedent) or consequent


# =============================================================================
# Section 3.7 — External Operation of Modes (state-transition guards)
# =============================================================================

# ---- Section 3.7.1 — Mode A (Contextual Expression) ----

def enter_A(kappa, kappa_star, rho, rho_star, delta_dialog):
    """Construct: Mode A activation guard enter_A — Section 3.7.1.
    Equation implemented:
        enter_A:  kappa(t) >= kappa*  AND  rho(t) >= rho*  AND  delta_dialog(t) = 1
    """
    # kappa      -> kappa(t)
    # kappa_star -> kappa*
    # rho        -> rho(t)
    # rho_star   -> rho*
    # delta_dialog -> delta_dialog(t) in {0,1}
    return (kappa >= kappa_star) and (rho >= rho_star) and (delta_dialog == 1)


def a_to_stabilization(receiver_response, instability):
    """Construct: Mode A exit transition A -> Stabilization — Section 3.7.1.
    Equation implemented:
        A -> Stabilization:
            R_receiver(t) in {acceptance, understanding, cooperative alignment}
            AND without instability
    """
    # receiver_response -> R_receiver(t): receiver-response category
    # instability       -> "without instability" flag (negated in the guard)
    return (receiver_response in {"acceptance", "understanding", "cooperative alignment"}) and (not instability)


def a_to_c(epsilon, epsilon_star, delta_dist, delta_dist_star, iota, iota_star):
    """Construct: Mode A exit transition A -> C — Section 3.7.1.
    Equation implemented:
        A -> C:  epsilon(t) > epsilon*  OR  delta_dist(t) > delta_dist*  OR  iota(t) > iota*
    """
    # epsilon        -> epsilon(t)
    # epsilon_star   -> epsilon*
    # delta_dist     -> delta_dist(t)
    # delta_dist_star -> delta_dist*
    # iota           -> iota(t)
    # iota_star      -> iota*
    return (epsilon > epsilon_star) or (delta_dist > delta_dist_star) or (iota > iota_star)


# ---- Section 3.7.2 — Mode B (Contextual Exploration) ----

def enter_B(kappa, kappa_star, rho, rho_star, delta_dialog):
    """Construct: Mode B activation guard enter_B — Section 3.7.2.
    Equation implemented:
        enter_B:  ( kappa(t) < kappa*  OR  rho(t) < rho*
                    OR  ( kappa(t) < kappa*  AND  rho(t) < rho* ) )
                  AND  delta_dialog(t) = 1
    The redundant third disjunct is preserved verbatim (no cleanup).
    """
    # kappa        -> kappa(t)
    # kappa_star   -> kappa*
    # rho          -> rho(t)
    # rho_star     -> rho*
    # delta_dialog -> delta_dialog(t) in {0,1}
    return (((kappa < kappa_star) or (rho < rho_star) or ((kappa < kappa_star) and (rho < rho_star)))
            and (delta_dialog == 1))


def b_to_a(requires_articulation):
    """Construct: Mode B termination condition B -> A — Section 3.7.2.
    Equation implemented:
        B -> A:  contextualized intention requires articulation
    """
    # requires_articulation -> "contextualized intention requires articulation"
    return requires_articulation


def b_to_stabilization(requires_articulation, epsilon, epsilon_star, delta_dist, delta_dist_star):
    """Construct: Mode B termination condition B -> Stabilization — Section 3.7.2.
    Equation implemented (verbatim — note that iota does NOT appear in this
    guard in the source):
        B -> Stabilization:
            no contextualized intention articulation is required
            AND NOT( epsilon > epsilon*  OR  delta_dist > delta_dist* )
    """
    # requires_articulation -> "no contextualized intention articulation is required" (negated flag)
    # epsilon               -> epsilon
    # epsilon_star          -> epsilon*
    # delta_dist            -> delta_dist
    # delta_dist_star       -> delta_dist*
    return (not requires_articulation) and (not ((epsilon > epsilon_star) or (delta_dist > delta_dist_star)))


def b_to_c(epsilon, epsilon_star, delta_dist, delta_dist_star, iota, iota_star):
    """Construct: Mode B exit transition B -> C — Section 3.7.2.
    Equation implemented:
        B -> C:  epsilon(t) > epsilon*  OR  delta_dist(t) > delta_dist*  OR  iota(t) > iota*
    """
    # epsilon        -> epsilon(t)
    # epsilon_star   -> epsilon*
    # delta_dist     -> delta_dist(t)
    # delta_dist_star -> delta_dist*
    # iota           -> iota(t)
    # iota_star      -> iota*
    return (epsilon > epsilon_star) or (delta_dist > delta_dist_star) or (iota > iota_star)


def b_to_interruption(delta_dialog_interrupted_deferred_or_structurally_constrained):
    """Construct: Mode B exit transition B -> Interruption — Section 3.7.2.
    Equation implemented:
        B -> Interruption:  delta_dialog(t) interrupted, deferred, or
                            structurally constrained
    """
    # delta_dialog_interrupted_deferred_or_structurally_constrained -> "delta_dialog(t) interrupted, deferred, or structurally constrained"
    return delta_dialog_interrupted_deferred_or_structurally_constrained


def mode_b_operable(mode_b_operable_flag, delta_dialog):
    """Construct: Mode-B-operable implication — Section 3.7.2.
    Equation implemented (material implication):
        Mode-B-operable(t)  =>  delta_dialog(t) = 1
    ("The source specifies Mode B operates only while dialogue is available.")
    """
    # mode_b_operable_flag -> Mode-B-operable(t)
    # delta_dialog          -> delta_dialog(t) in {0,1}
    return (not mode_b_operable_flag) or (delta_dialog == 1)


# ---- Section 3.7.3 — Mode C (Recursive Proportional Alignment) ----

def enter_C(epsilon, epsilon_star, delta_dist, delta_dist_star, iota, iota_star, delta_dialog):
    """Construct: Mode C activation guard enter_C — Section 3.7.3.
    Equation implemented:
        enter_C:  epsilon(t) > epsilon*  OR  delta_dist(t) > delta_dist*
                  OR  iota(t) > iota*  OR  delta_dialog(t) = 0
    """
    # epsilon        -> epsilon(t)
    # epsilon_star   -> epsilon*
    # delta_dist     -> delta_dist(t)
    # delta_dist_star -> delta_dist*
    # iota           -> iota(t)
    # iota_star      -> iota*
    # delta_dialog   -> delta_dialog(t) in {0,1}
    return ((epsilon > epsilon_star) or (delta_dist > delta_dist_star)
            or (iota > iota_star) or (delta_dialog == 0))


def mode_c_branch(delta_dialog, reciprocal_clarification_available):
    """Construct: Mode C sub-mode branching (Mode-C-branch) — Section 3.7.3.
    Equation implemented:
        Mode-C-branch(t) = Self-Alignment   if delta_dialog(t) = 0 OR reciprocal
                                              clarification is not immediately
                                              available, interrupted, deferred,
                                              or structurally constrained
                           Shared-Alignment if delta_dialog(t) = 1 AND
                                              reciprocal clarification available
    (Distinct from the Section 3.3 Mode-C-subform, which uses delta_dialog only;
    both are written in the source, so both are implemented separately.)
    """
    # delta_dialog                        -> delta_dialog(t) in {0,1}
    # reciprocal_clarification_available  -> "reciprocal clarification available"
    if (delta_dialog == 1) and reciprocal_clarification_available:
        return "Shared-Alignment"
    if (delta_dialog == 0) or (not reciprocal_clarification_available):
        return "Self-Alignment"
    # UNSPECIFIED IN SOURCE MATH: behavior undefined for this case —
    # delta_dialog(t) outside {0, 1} is not defined in the source.
    return None


# ---- Section 3.7.3.1 — Self-Alignment (intrapersonal) ----

def self_alignment_termination(i_avail, i_req, epsilon, epsilon_star, delta_dist, delta_dist_star):
    """Construct: Self-Alignment termination guard — Section 3.7.3.1.
    Equation implemented:
        Self-Alignment -> {A, B, Stabilization}:
            I_avail(t) >= I_req(t)  AND  epsilon <= epsilon*  AND  delta_dist <= delta_dist*
    The target is the SET {A, B, Stabilization}; the choice among them is not
    specified in the source (the flow names "Mode A for contextual expression,
    Mode B for relational building, or the Stabilization Handler for testing
    or termination").
    """
    # i_avail         -> I_avail(t)
    # i_req           -> I_req(t)
    # epsilon         -> epsilon
    # epsilon_star    -> epsilon*
    # delta_dist      -> delta_dist
    # delta_dist_star -> delta_dist*
    return (i_avail >= i_req) and (epsilon <= epsilon_star) and (delta_dist <= delta_dist_star)


def self_alignment_escalation(refinement_remains_insufficient, reciprocal_clarification_later_available):
    """Construct: Self-Alignment escalation guard — Section 3.7.3.1.
    Equation implemented:
        Self-Alignment -> Shared-Alignment or B:
            refinement remains insufficient
            AND reciprocal clarification later becomes available
    """
    # refinement_remains_insufficient           -> "refinement remains insufficient"
    # reciprocal_clarification_later_available   -> "reciprocal clarification later becomes available"
    return refinement_remains_insufficient and reciprocal_clarification_later_available


# ---- Section 3.7.3.2 — Shared-Alignment (interpersonal, recursive) ----

def shared_alignment_loop(t, i_avail, i_req, delta_dialog, W, whys,
                          acknowledgment, emit, receive_refinement):
    """Construct: Shared-Alignment bounded recursive loop — Section 3.7.3.2.
    Equation implemented (the source's while-structure, translated verbatim):
        while ( I_avail(t) < I_req(t) ) and delta_dialog(t) = 1 do:
            Acknowledgment(W(t)) ; emit {Why_i}_{i=1}^{n} ;
            receive refinement ; t <- t + 1
        end while ; transition to Stabilization Handler
    """
    # t                   -> t: discrete interaction step (incremented by the loop per t <- t + 1)
    # i_avail             -> I_avail(t): callable, re-evaluated at each t
    # i_req               -> I_req(t): callable, re-evaluated at each t
    # delta_dialog        -> delta_dialog(t) in {0,1}: callable, re-evaluated at each t
    # W                   -> W(t): callable yielding the What being acknowledged at each t
    # whys                -> {Why_i}_{i=1}^{n}: the provisional contextual attributions emitted each iteration
    # acknowledgment      -> Acknowledgment(.): acknowledgment action
    # emit                -> emit(.): emission action
    # receive_refinement  -> "receive refinement": refinement-reception action
    while (i_avail(t) < i_req(t)) and (delta_dialog(t) == 1):
        acknowledgment(W(t))
        emit(whys)
        receive_refinement()
        t = t + 1
    # end while; transition to Stabilization Handler
    return Q_STAB


def shared_alignment_bypass(i_avail_at_t0, i_req_at_t0):
    """Construct: Shared-Alignment bypass condition — Section 3.7.3.2.
    Equation implemented:
        Shared-Alignment -> Stabilization (direct):  I_avail(t_0) >= I_req(t_0)
    """
    # i_avail_at_t0 -> I_avail(t_0)
    # i_req_at_t0   -> I_req(t_0)
    return i_avail_at_t0 >= i_req_at_t0


def shared_alignment_interruption(reciprocal_clarification_interrupted_deferred_or_structurally_constrained):
    """Construct: Shared-Alignment interruption condition — Section 3.7.3.2.
    Equation implemented:
        Shared-Alignment -> Interruption:
            reciprocal clarification is interrupted, deferred, or structurally
            constrained
    """
    # reciprocal_clarification_interrupted_deferred_or_structurally_constrained -> "reciprocal clarification is interrupted, deferred, or structurally constrained"
    return reciprocal_clarification_interrupted_deferred_or_structurally_constrained


# ---- Section 3.7.3.3 — Recursive Alignment Continuity ----

# Construct fact: "Recursive alignment in Shared-Alignment only" — Section 3.7.3.3.
RECURSIVE_ALIGNMENT_CONTAINMENT = "Recursive alignment ∈ Shared-Alignment only"


def recursive_alignment_continues(i_avail, i_req):
    """Construct: Recursive Alignment Continuity — Section 3.7.3.3.
    Equation implemented:
        Recursive alignment ∈ Shared-Alignment only,
        ceases when I_avail(t) >= I_req(t)
    The predicate returns whether recursion continues (i.e. I_avail(t) < I_req(t)).
    """
    # i_avail -> I_avail(t)
    # i_req   -> I_req(t)
    return i_avail < i_req


# ---- Section 3.7.4 — Stabilization Handler ----

def stab_to_closure(delta_reg):
    """Construct: Stabilization Handler test outcome Stab -> Closure —
    Section 3.7.4.
    Equation implemented:
        Stab -> Closure:  Delta_regulatory(t) > 0
        (observed regulatory shift toward collaborative or neutral engagement)
    """
    # delta_reg -> Delta_regulatory(t)
    return delta_reg > 0


def stab_to_b_or_c(delta_reg):
    """Construct: Stabilization Handler test outcome Stab -> {B, C} —
    Section 3.7.4.
    Equation implemented:
        Stab -> {B, C}:  Delta_regulatory(t) <= 0
        (continued anger, defensiveness, or rejection of the proposed forward
         step)
    """
    # delta_reg -> Delta_regulatory(t)
    return delta_reg <= 0


def stab_self_loop(requires_incremental_articulation, constitutes_reentry_into_prior_modes, delta_reg):
    """Construct: Stabilization Handler Incremental Articulation self-loop
    guard — Section 3.7.4.
    Equation implemented:
        Guard condition:
            Requires(incremental articulation)
            AND NOT( constitute re-entry into prior modes )
            AND Delta_regulatory(t) >= 0
    """
    # requires_incremental_articulation    -> Requires(incremental articulation)
    # constitutes_reentry_into_prior_modes -> "constitute re-entry into prior modes" (negated in the guard)
    # delta_reg                            -> Delta_regulatory(t)
    return (requires_incremental_articulation
            and (not constitutes_reentry_into_prior_modes)
            and (delta_reg >= 0))


# ---- Section 3.7.5 — Interruption Handler (Semi-Stabilized State) ----

def interruption_on_dialog_drop(delta_dialog_previous, delta_dialog_current,
                                partial_contextual_clarity_achieved,
                                most_recently_refined_what_why):
    """Construct: Interruption Handler pause structure (on delta_dialog:
    1 -> 0) — Section 3.7.5.
    Equation implemented:
        on delta_dialog(t): 1 -> 0 (when partial contextual clarity has been
        achieved but dialogue becomes temporarily interrupted or incomplete):
            state(t) <- Semi-Stabilized ;
            hold provisionally( most recently refined What-Why articulation ) ;
            temporarily shifts toward Self-Alignment in Mode C
    Source constraint preserved: "Temporary interruption does not invalidate
    the alignment process; it pauses its progression without forcing closure."
    """
    # delta_dialog_previous                  -> delta_dialog at the previous step
    # delta_dialog_current                   -> delta_dialog(t) at the current step
    # partial_contextual_clarity_achieved    -> "partial contextual clarity has been achieved"
    # most_recently_refined_what_why         -> most recently refined What-Why articulation (the (What, Why) state held provisionally)
    if (delta_dialog_previous == 1) and (delta_dialog_current == 0) and partial_contextual_clarity_achieved:
        held = most_recently_refined_what_why  # hold provisionally(...)
        return {"state": "Semi-Stabilized",
                "held_what_why": held,
                "routing": Q_C_SELF}
    # UNSPECIFIED IN SOURCE MATH: behavior undefined for this case —
    # a 1 -> 0 dialog drop without partial contextual clarity is not covered
    # by the written guard; the case is left unhandled.


def interruption_on_dialog_resume(delta_dialog_previous, delta_dialog_current,
                                  i_avail, i_req, epsilon, epsilon_star,
                                  delta_dist, delta_dist_star):
    """Construct: Interruption Handler resume structure (on delta_dialog:
    0 -> 1) — Section 3.7.5.
    Equation implemented:
        on delta_dialog(t): 0 -> 1 (When reciprocal clarification resumes:
        proceeds according to the contextual clarity conditions defined in
        Self-Alignment)
    The Self-Alignment clarity conditions are the Section 3.7.3.1 termination
    guard (the source explicitly directs to it); when the guard holds, the
    permitted target set is {A, B, Stabilization}, and otherwise the process
    remains in Self-Alignment per the Section 3.8.3 Self-Alignment flow
    ("Continue intrapersonal refinement").
    """
    # delta_dialog_previous -> delta_dialog at the previous step
    # delta_dialog_current  -> delta_dialog(t) at the current step
    # i_avail               -> I_avail(t)
    # i_req                 -> I_req(t)
    # epsilon               -> epsilon(t)
    # epsilon_star          -> epsilon*
    # delta_dist            -> delta_dist(t)
    # delta_dist_star       -> delta_dist*
    if (delta_dialog_previous == 0) and (delta_dialog_current == 1):
        if self_alignment_termination(i_avail, i_req, epsilon, epsilon_star, delta_dist, delta_dist_star):
            return {Q_A, Q_B, Q_STAB}
        return Q_C_SELF
    # UNSPECIFIED IN SOURCE MATH: behavior undefined for this case —
    # the handler is defined only for the 0 -> 1 dialog edge; the case is left
    # unhandled.


# ---- Section 3.7.6 — Cumulative Context Across Mode Transitions ----

def s_t(mode, operational_what, contextual_why):
    """Construct: ELM system state S(t) — Section 3.7.6.
    Equation implemented:
        S(t) = < Mode(t), Operational What(t), Contextual Why(t) >
    """
    # mode             -> Mode(t)
    # operational_what -> Operational What(t)
    # contextual_why   -> Contextual Why(t)
    return (mode, operational_what, contextual_why)


def cumulative_context_invariant(s_t_value, s_t_plus_1_value):
    """Construct: Cumulative Context invariant (Global Invariant) —
    Section 3.7.6.
    Equation implemented:
        FOR ALL transition at t:  S(t) -> S(t+1)  =>
            Operational What(t+1) = Operational What(t)
            AND Contextual Why(t+1) = Contextual Why(t)
    (ensuring that previously established context is preserved throughout
    interactional routing)
    """
    # s_t_value         -> S(t)   = < Mode(t), Operational What(t), Contextual Why(t) >
    # s_t_plus_1_value  -> S(t+1) = < Mode(t+1), Operational What(t+1), Contextual Why(t+1) >
    return (s_t_plus_1_value[1] == s_t_value[1]) and (s_t_plus_1_value[2] == s_t_value[2])


# =============================================================================
# Section 3.2 / 3.7 — The state-transition function delta (concretely
# specified by Section 3.3 mode-selection logic and Section 3.7 transitions)
# =============================================================================

def delta(q, sigma, kappa_star, rho_star, epsilon_star, delta_dist_star, iota_star):
    """Construct: state-transition function delta of the ELM-FSM — Section 3.2
    ("delta: Q x Sigma -> Q ... defined by Section 3.3 mode-selection logic
    and Section 3.7 external transitions").
    Each branch below cites and applies the corresponding Section 3.3 / 3.7
    guard function implemented above (the source composes delta from exactly
    these guards, so the composition is source-sanctioned, not a merge).
    Precedence note: where several guards of one state are simultaneously
    enabled, the source does not specify precedence; guards are checked in the
    order the source lists them.
    Where the source's transition target is written as a SET (e.g.
    "Self-Alignment -> {A, B, Stabilization}"), delta returns that set of
    permitted targets because the source does not disambiguate the choice.
    """
    # q              -> q: current state in Q
    # sigma          -> sigma in Sigma: contextual signal (ContextualSignal)
    # kappa_star     -> kappa*  (NOT numerically specified in the source)
    # rho_star       -> rho*   (NOT numerically specified in the source)
    # epsilon_star   -> epsilon* (NOT numerically specified in the source)
    # delta_dist_star -> delta_dist* (NOT numerically specified in the source)
    # iota_star      -> iota*  (NOT numerically specified in the source)

    if q == Q_INPUT:
        # Section 3.3 Mode Selection Logic from the initial state.
        m = mode_selection(sigma.kappa, kappa_star, sigma.rho, rho_star,
                           sigma.epsilon, epsilon_star, sigma.delta_dist,
                           delta_dist_star, sigma.iota, iota_star, sigma.delta_dialog)
        if m == MODE_A:
            return Q_A
        if m == MODE_B:
            return Q_B
        if m == MODE_C:
            # Section 3.3 Mode C duality (Mode-C-subform).
            if mode_c_subform(sigma.delta_dialog) == "Shared-Alignment":
                return Q_C_SHARED
            return Q_C_SELF
        # UNSPECIFIED IN SOURCE MATH: mode_selection returned no mode.
        return None

    if q == Q_A:
        # Section 3.7.1 exit transitions (listed order: Stabilization, then C).
        if a_to_stabilization(sigma.receiver_response, sigma.instability):
            return Q_STAB
        if a_to_c(sigma.epsilon, epsilon_star, sigma.delta_dist, delta_dist_star,
                  sigma.iota, iota_star):
            # Section 3.3 Mode-C duality determines the subform.
            if mode_c_subform(sigma.delta_dialog) == "Shared-Alignment":
                return Q_C_SHARED
            return Q_C_SELF
        # UNSPECIFIED IN SOURCE MATH: no exit guard enabled; no A self-loop is
        # written in the source, so the case is left unhandled (state returned
        # unchanged).
        return q

    if q == Q_B:
        # Section 3.7.2 transitions (listed order: B->A, B->Stabilization,
        # B->C, B->Interruption).
        if b_to_a(sigma.requires_articulation):
            return Q_A
        if b_to_stabilization(sigma.requires_articulation, sigma.epsilon,
                              epsilon_star, sigma.delta_dist, delta_dist_star):
            return Q_STAB
        if b_to_c(sigma.epsilon, epsilon_star, sigma.delta_dist, delta_dist_star,
                  sigma.iota, iota_star):
            if mode_c_subform(sigma.delta_dialog) == "Shared-Alignment":
                return Q_C_SHARED
            return Q_C_SELF
        if b_to_interruption(sigma.dialog_interrupted_deferred_or_structurally_constrained):
            return Q_INT
        # UNSPECIFIED IN SOURCE MATH: no exit guard enabled; no B self-loop is
        # written in the source, so the case is left unhandled (state returned
        # unchanged).
        return q

    if q == Q_C_SELF:
        # Section 3.7.3.1 Self-Alignment terminations (listed order).
        if self_alignment_termination(sigma.i_avail, sigma.i_req, sigma.epsilon,
                                      epsilon_star, sigma.delta_dist, delta_dist_star):
            # Target set {A, B, Stabilization}: the choice among them is
            # UNSPECIFIED IN SOURCE MATH; the set is returned.
            return {Q_A, Q_B, Q_STAB}
        if self_alignment_escalation(sigma.refinement_remains_insufficient,
                                     sigma.reciprocal_clarification_available):
            # Target "Shared-Alignment or B": the choice is UNSPECIFIED IN
            # SOURCE MATH; the set is returned.
            return {Q_C_SHARED, Q_B}
        # Self-Alignment refinement continues (Section 3.8.3 flow:
        # "Continue intrapersonal refinement").
        return Q_C_SELF

    if q == Q_C_SHARED:
        # Section 3.7.3.2 Shared-Alignment transitions.
        if not recursive_alignment_continues(sigma.i_avail, sigma.i_req):
            # Bypass condition / end-while: I_avail(t) >= I_req(t) ->
            # transition to Stabilization Handler.
            return Q_STAB
        if shared_alignment_interruption(sigma.dialog_interrupted_deferred_or_structurally_constrained):
            return Q_INT
        if sigma.delta_dialog != 1:
            # Loop condition ( I_avail(t) < I_req(t) AND delta_dialog(t) = 1 )
            # fails on dialogue availability while information remains
            # insufficient: routed per the Section 3.7.5 Interruption Handler
            # (on delta_dialog: 1 -> 0).
            return Q_INT
        # Bounded recursive loop continues (Section 3.7.3.2 / 3.7.3.3).
        return Q_C_SHARED

    if q == Q_STAB:
        # Section 3.7.4 test outcomes. Order: Closure (Delta > 0), then the
        # Incremental Articulation self-loop (Delta >= 0), then {B, C}
        # (Delta <= 0). This order keeps every written guard reachable; at
        # Delta = 0 both the self-loop and {B, C} guards are enabled and
        # precedence is UNSPECIFIED IN SOURCE MATH.
        if stab_to_closure(sigma.delta_reg):
            # Accepting terminal state per F = {q_stab | CSC satisfied}
            # (Section 3.2) reached via Stab -> Closure.
            return Q_CLOSURE
        if stab_self_loop(sigma.requires_incremental_articulation,
                          sigma.constitutes_reentry_into_prior_modes, sigma.delta_reg):
            return Q_STAB
        if stab_to_b_or_c(sigma.delta_reg):
            # Section 3.8.4: "Return to Mode B or Mode C based on Mode
            # Selection Criteria."
            m = mode_selection(sigma.kappa, kappa_star, sigma.rho, rho_star,
                               sigma.epsilon, epsilon_star, sigma.delta_dist,
                               delta_dist_star, sigma.iota, iota_star, sigma.delta_dialog)
            if m == MODE_B:
                return Q_B
            if m == MODE_C:
                if mode_c_subform(sigma.delta_dialog) == "Shared-Alignment":
                    return Q_C_SHARED
                return Q_C_SELF
            # UNSPECIFIED IN SOURCE MATH: Section 3.7.4 restricts this exit to
            # {B, C} but Mode Selection may yield A; the case is left
            # unhandled.
            return None
        # UNSPECIFIED IN SOURCE MATH: no Stabilization exit guard enabled.
        return q

    if q == Q_INT:
        # Section 3.7.5 Interruption Handler (Semi-Stabilized State).
        if sigma.delta_dialog == 1:
            # on delta_dialog: 0 -> 1 — proceeds according to the contextual
            # clarity conditions defined in Self-Alignment (Section 3.7.3.1).
            if self_alignment_termination(sigma.i_avail, sigma.i_req, sigma.epsilon,
                                          epsilon_star, sigma.delta_dist, delta_dist_star):
                return {Q_A, Q_B, Q_STAB}
            return Q_C_SELF
        # delta_dialog(t) = 0: Semi-Stabilized hold, temporarily shifts toward
        # Self-Alignment in Mode C.
        return Q_C_SELF

    # UNSPECIFIED IN SOURCE MATH: q is not a state of Q_STATES; behavior
    # undefined for this case (left unhandled).
    return None


def elm_fsm(kappa_star, rho_star, epsilon_star, delta_dist_star, iota_star):
    """Construct: ELM-FSM assembly — Section 3.2.
    Equation implemented:
        ELM-FSM = ( Q, Sigma, delta, q_0, F )
    with delta bound to the Section 3.3/3.7 transition logic and the five
    threshold parameters (all numerically unspecified in the source; no
    defaults are supplied).
    """
    # kappa_star      -> kappa*
    # rho_star        -> rho*
    # epsilon_star    -> epsilon*
    # delta_dist_star -> delta_dist*
    # iota_star       -> iota*
    def _delta(q, sigma):
        return delta(q, sigma, kappa_star, rho_star, epsilon_star, delta_dist_star, iota_star)
    # Q    -> Q_STATES (Q ⊇ {q_A, q_B, q_C_self, q_C_shared, q_stab, q_int})
    # Sigma -> ContextualSignal (input alphabet of contextual signals)
    # delta -> _delta (bound to Section 3.3 / 3.7 logic)
    # q_0  -> Q_INPUT (initial state on Event perception)
    # F    -> {Q_STAB} qualified by "CSC satisfied" (F = {q_stab | CSC satisfied})
    return ELMFSM(q=Q_STATES, sigma=ContextualSignal, delta=_delta,
                  q0=Q_INPUT, f=frozenset({Q_STAB}))


# =============================================================================
# Section 3.8 — External Operational Flow Across Modes
# (directed execution paths and compact operational patterns)
# =============================================================================

# Construct: Mode A operational flow (directed execution path) — Section 3.8.1.
OPERATIONAL_FLOW_MODE_A = (
    "Internal Intention",
    "Contextual Grounding (Why)",
    "Alignment of Why with Intended What",
    "Context-Intention Aligned Expression",
)

# Construct: Mode B operational flow — Section 3.8.2.
OPERATIONAL_FLOW_MODE_B = (
    "Observed What",
    "Recognition of Missing Context",
    "Provisional Why(s) (Inquiry)",
    "Contextual Clarification through Dialogue",
    "Context Refinement",
    "Refined Understanding and Context Appears Sufficient",
)

# Construct: Mode C Self-Alignment operational flow (Early Regulation) — Section 3.8.3.
OPERATIONAL_FLOW_C_SELF_EARLY = (
    "Event",
    "Observed or Interpretive What",
    "Provisional Why",
    "Contextually Framed Interpretation",
    "Proportional Thought",
    "Intrapersonal Refinement through Observation",
    "Contextual Information Appears Sufficient and no Interpretive Distortion or Emotional Escalation (is present)",
    "Transition to Mode A for contextual expression, Mode B for relational building, or to the Stabilization Handler for testing or termination",
    "Additional Contextual Clarity (if required)",
    "Continue intrapersonal refinement...",
)

# Construct: Mode C Self-Alignment operational flow (Late Regulation) — Section 3.8.3.
OPERATIONAL_FLOW_C_SELF_LATE = (
    "Event",
    "Automatic Interpretation",
    "Thought",
    "Recognition of Missing Context",
    "Return to Event",
    "Observed or Interpretive What",
    "Provisional Why",
    "Reconstructed Contextually Framed Interpretation",
    "Proportional Thought",
    "Intrapersonal Refinement through Observation",
    "Contextual Information Appears Sufficient and no Interpretive Distortion or Emotional Escalation (is present)",
    "Transition to Mode A for contextual expression, Mode B for relational building, or to the Stabilization Handler for testing or termination",
    "Additional Contextual Clarity (if required)",
    "Continue intrapersonal refinement...",
)

# Construct: Mode C Shared-Alignment operational flow (Recursive) — Section 3.8.3.
OPERATIONAL_FLOW_C_SHARED = (
    "Observed or Interpretive What",
    "Acknowledgment",
    "Provisional Why",
    "Clarificatory Inquiry",
    "Context Refinement",
    "Repeat until Context Appears Sufficient",
)

# Construct: Stabilization Handler operational flow — Section 3.8.4.
OPERATIONAL_FLOW_STABILIZATION = (
    "Perceived Contextual Clarity",
    "Acknowledgment (when relational response is required)",
    "Proportional Forward Step or Supportive Intention (if testing required)",
    "Evaluation of the Contextual Sufficiency Criterion (Regulatory Shift Test with combined pattern)",
)
OPERATIONAL_FLOW_STAB_SUCCESS = ("Success", "Closure")
OPERATIONAL_FLOW_STAB_FAILURE = ("Failure", "Return to Mode B or Mode C based on Mode Selection Criteria")

# Construct: Interruption Handler operational flow — Section 3.8.5.
OPERATIONAL_FLOW_INTERRUPTION = (
    "Partially Refined What-Why",
    "Semi-Stabilized Interpretation",
    "Self-Alignment (Hold)",
    "Reflective Observation",
    "Dialogue Resumes",
    "Mode Transition",
)


def pattern_a(why, intended_what, ordered_combine):
    """Construct: Compact Operational Pattern of Mode A — Section 3.8.1.
    Equation implemented:
        Pattern_A(t) = Why(t) (+) Intended What(t)  OR
                       Intended What(t) (+) Why(t)
    (where (+) denotes ordered or integrated combination, "sequentially or
    within a unified expression"). The disjunction is returned as the pair of
    admissible orderings.
    """
    # why             -> Why(t)
    # intended_what   -> Intended What(t)
    # ordered_combine -> (+): ordered/integrated combination operator (form not numerically specified in the source)
    return (ordered_combine(why, intended_what), ordered_combine(intended_what, why))


def pattern_b(observed_what, provisional_whys, ordered_combine):
    """Construct: Compact Operational Pattern of Mode B — Section 3.8.2.
    Equation implemented:
        Pattern_B(t) = Observed What(t) (+) {Why_i(t)}_{Inquiry — stays open
                       to Collaborative Refinement}
    """
    # observed_what   -> Observed What(t)
    # provisional_whys -> {Why_i(t)}_{Inquiry — stays open to Collaborative Refinement}
    # ordered_combine -> (+): ordered/integrated combination operator
    return ordered_combine(observed_what, provisional_whys)


def pattern_c_self(operational_what, provisional_whys, ordered_combine):
    """Construct: Compact Operational Pattern of Mode C Self-Alignment —
    Section 3.8.3.
    Equation implemented:
        Pattern_{C,self}(t) = Operational What(t) (+) {Why_i(t)}_{Held with
                              epistemic humility — stays open to Observational
                              Refinement}
    """
    # operational_what -> Operational What(t)
    # provisional_whys -> {Why_i(t)}_{Held with epistemic humility — stays open to Observational Refinement}
    # ordered_combine  -> (+): ordered/integrated combination operator
    return ordered_combine(operational_what, provisional_whys)


def pattern_c_shared(operational_what, provisional_whys, acknowledgment, ordered_combine):
    """Construct: Compact Operational Pattern of Mode C Shared-Alignment —
    Section 3.8.3.
    Equation implemented:
        Pattern_{C,shared}(t) = Acknowledgment of Operational What(t) (+)
                                {Why_i(t)}_{Inquiry — stays open to Recursive
                                Collaborative Refinement}
    """
    # operational_what -> Operational What(t)
    # provisional_whys -> {Why_i(t)}_{Inquiry — stays open to Recursive Collaborative Refinement}
    # acknowledgment   -> Acknowledgment(.) of the Operational What
    # ordered_combine  -> (+): ordered/integrated combination operator
    return ordered_combine(acknowledgment(operational_what), provisional_whys)


def pattern_stab_relational(clarified_what, clarified_why, acknowledgment,
                            proportional_forward_step_or_supportive_intention,
                            forward_step_required, ordered_combine):
    """Construct: Compact Operational Pattern of the Stabilization Handler
    (Relational Response, if required) — Section 3.8.4.
    Equation implemented:
        Pattern_Stab_Relational(t) = Acknowledgment of Clarified What and Why
                                     (must) (+) Proportional Forward Step /
                                     Supportive Intention (if required)
    """
    # clarified_what  -> Clarified What
    # clarified_why   -> Clarified Why
    # acknowledgment  -> Acknowledgment of Clarified What and Why (must)
    # proportional_forward_step_or_supportive_intention -> Proportional Forward Step / Supportive Intention
    # forward_step_required -> "(if required)" qualifier
    # ordered_combine -> (+): ordered/integrated combination operator
    ack = acknowledgment(clarified_what, clarified_why)  # must
    if forward_step_required:
        return ordered_combine(ack, proportional_forward_step_or_supportive_intention)
    # UNSPECIFIED IN SOURCE MATH: behavior undefined for this case —
    # the pattern's content when no forward step is required is not written;
    # the mandatory acknowledgment alone is returned.
    return ack


def pattern_stab_testing(clarified_what, clarified_why, acknowledgment,
                         proportional_forward_step, ordered_combine):
    """Construct: Compact Operational Pattern of the Stabilization Handler
    (If Testing is Required) — Section 3.8.4.
    Equation implemented:
        Pattern_Stab_Testing(t) = Acknowledgment of Clarified What and Why
                                  (must) (+) Proportional Forward Step (must)
    """
    # clarified_what         -> Clarified What
    # clarified_why          -> Clarified Why
    # acknowledgment         -> Acknowledgment of Clarified What and Why (must)
    # proportional_forward_step -> Proportional Forward Step (must)
    # ordered_combine        -> (+): ordered/integrated combination operator
    return ordered_combine(acknowledgment(clarified_what, clarified_why), proportional_forward_step)


def pattern_int(partially_refined_what_why, self_alignment_action, ordered_combine):
    """Construct: Compact Operational Pattern of the Interruption Handler —
    Section 3.8.5.
    Equation implemented:
        Pattern_Int(t) = Partially Refined What-Why(t) (+) Self-Alignment
                         (Observational Refinement or Mode Transition)
    """
    # partially_refined_what_why -> Partially Refined What-Why(t)
    # self_alignment_action       -> Self-Alignment (Observational Refinement or Mode Transition)
    # ordered_combine             -> (+): ordered/integrated combination operator
    return ordered_combine(partially_refined_what_why, self_alignment_action)


# =============================================================================
# Section 3.9 — General Structural Classification (5 layers + 1 cross-mode
#               safeguard)
# =============================================================================

# Construct: ELM structural layer set L_ELM — Section 3.9.
# Equation implemented:
#     L_ELM = { L1_input, L2_selection, L3_processing, L4_stabilization,
#               L5_interruption, Sigma_grounding }
ELM_LAYERS = frozenset({
    "L1_input",          # L1_input — Input Layer: e in E triggers IVP(t_0)
    "L2_selection",      # L2_selection — Regulatory Selection Layer: Mode Selection Logic (Mode(t) per Section 3.3)
    "L3_processing",     # L3_processing — Regulatory Processing Layer: Modes {A,B,C} with Mode C subforms {Self-Alignment, Shared-Alignment}
    "L4_stabilization",  # L4_stabilization — Stabilization Layer: enters when CSC(t) = 1
    "L5_interruption",   # L5_interruption — Interruption Layer: Interruption Handler preserves state and routes to Self-Alignment
    "Sigma_grounding",   # Sigma_grounding — Contextual Grounding Constraint (cross-mode safeguard)
})


def sigma_grounding_constraint(why_is_context_based, why_is_identity_level_framing,
                               why_is_motive_assumptive_framing, why_is_proportionate,
                               why_is_non_accusatory, why_is_open_to_clarification):
    """Construct: Contextual Grounding Constraint (cross-mode safeguard)
    Sigma_grounding — Section 3.9.
    Equation implemented:
        FOR ALL t, FOR ALL Why(t) in Mode(t):
            Why(t) in context-based explanations
            AND Why(t) NOT in { identity-level framing, motive-assumptive framing }
            AND proportionate( Why(t) )
            AND non-accusatory( Why(t) )
            AND open_to_clarification( Why(t) )
    The three articulation predicates are qualitative Boolean predicates per
    the source ("The source does not numerically operationalize these"), so
    they are supplied as inputs.
    """
    # why_is_context_based            -> Why(t) in context-based explanations
    # why_is_identity_level_framing   -> Why(t) in {identity-level framing} (negated in the constraint)
    # why_is_motive_assumptive_framing -> Why(t) in {motive-assumptive framing} (negated in the constraint)
    # why_is_proportionate            -> proportionate(Why(t))
    # why_is_non_accusatory           -> non-accusatory(Why(t))
    # why_is_open_to_clarification    -> open_to_clarification(Why(t))
    return (why_is_context_based
            and (not why_is_identity_level_framing)
            and (not why_is_motive_assumptive_framing)
            and why_is_proportionate
            and why_is_non_accusatory
            and why_is_open_to_clarification)


# =============================================================================
# Section 3.10 — External System Architecture
# =============================================================================

# Construct: ELM system-property statement — Section 3.10.
# Equation implemented:
#     ELM |= deadlock-resistant AND defined termination conditions
#           AND fault-tolerant
ELM_SYSTEM_PROPERTIES = ("deadlock-resistant", "defined termination conditions", "fault-tolerant")


def termination_guarantee(csc_sequence, mode_sequence):
    """Construct: Termination guarantee — Section 3.10.
    Equation implemented:
        FOR ALL e in E:  EXISTS t_term < infinity  such that
            CSC(t_term) = 1  OR  Mode(t_term) = Self-Alignment (default
            fallback)
    Evaluated over the (finite) trajectory supplied: the guarantee holds if
    some step t satisfies CSC(t) = 1 or Mode(t) = Self-Alignment.
    """
    # csc_sequence  -> CSC(t) values along the trajectory (in {0, 1})
    # mode_sequence -> Mode(t) values along the trajectory
    return any((c == 1) or (m == "Self-Alignment") for c, m in zip(csc_sequence, mode_sequence))


# =============================================================================
# Section 3.11 — Key Regulatory Conditions
# =============================================================================

def c_insufficient_context(i_avail, i_req):
    """Construct: regulatory condition Insufficient Context — Section 3.11.
    Equation implemented:
        C_insuff(t) = 1[ I_avail(t) < I_req(t) ]
    """
    # i_avail -> I_avail(t)
    # i_req   -> I_req(t)
    return int(i_avail < i_req)


def c_relational_unfamiliarity(rho, rho_star):
    """Construct: regulatory condition Relational Unfamiliarity — Section 3.11.
    Equation implemented:
        C_unfam(t) = 1[ rho(t) < rho* ]
    """
    # rho      -> rho(t)
    # rho_star -> rho*
    return int(rho < rho_star)


def c_interpretive_distortion(delta_dist, delta_dist_star):
    """Construct: regulatory condition Interpretive Distortion — Section 3.11.
    Equation implemented:
        C_dist(t) = 1[ delta_dist(t) > delta_dist* ]
    """
    # delta_dist      -> delta_dist(t)
    # delta_dist_star -> delta_dist*
    return int(delta_dist > delta_dist_star)


def c_emotional_activation(epsilon, epsilon_star):
    """Construct: regulatory condition Emotional Activation — Section 3.11.
    Equation implemented:
        C_emot(t) = 1[ epsilon(t) > epsilon* ]
    """
    # epsilon      -> epsilon(t)
    # epsilon_star -> epsilon*
    return int(epsilon > epsilon_star)


def c_relational_instability(iota, iota_star):
    """Construct: regulatory condition Relational Instability — Section 3.11.
    Equation implemented:
        C_inst(t) = 1[ iota(t) > iota* ]
    """
    # iota      -> iota(t)
    # iota_star -> iota*
    return int(iota > iota_star)


def c_dialogue_unavailability(delta_dialog):
    """Construct: regulatory condition Dialogue Unavailability — Section 3.11.
    Equation implemented:
        C_dialog|off(t) = 1[ delta_dialog(t) = 0 ]
    """
    # delta_dialog -> delta_dialog(t) in {0,1}
    return int(delta_dialog == 0)


def coupling_rule(c_insuff, unmanaged_interpretive_velocity, pic_value):
    """Construct: coupling rule — Section 3.11.
    Equation implemented (material implication):
        C_insuff(t) = 1  AND unmanaged Interpretive Velocity
            =>  PIC(t) -> 1
    """
    # c_insuff                       -> C_insuff(t) in {0, 1}
    # unmanaged_interpretive_velocity -> "unmanaged Interpretive Velocity"
    # pic_value                      -> PIC(t) in {0, 1}
    antecedent = (c_insuff == 1) and unmanaged_interpretive_velocity
    return (not antecedent) or (pic_value == 1)


def routing_consequence_unfamiliarity(c_unfam, delta_dialog):
    """Construct: routing consequence (relational unfamiliarity) — Section 3.11.
    Equation implemented:
        C_unfam(t) = 1  AND  delta_dialog = 1
            =>  cautious exploration (Mode B)
    """
    # c_unfam       -> C_unfam(t) in {0, 1}
    # delta_dialog  -> delta_dialog(t) in {0,1}
    if (c_unfam == 1) and (delta_dialog == 1):
        return MODE_B
    # UNSPECIFIED IN SOURCE MATH: the implication's guard is not enabled; no
    # routing is dictated and the case is left unhandled.
    return None


def routing_consequence_alignment(c_dist, c_emot, c_inst):
    """Construct: routing consequence (alignment conditions) — Section 3.11.
    Equation implemented:
        ( C_dist(t) OR C_emot(t) OR C_inst(t) ) = 1
            =>  Recursive Proportional Alignment (Mode C)
    """
    # c_dist -> C_dist(t) in {0, 1}
    # c_emot -> C_emot(t) in {0, 1}
    # c_inst -> C_inst(t) in {0, 1}
    if (c_dist == 1) or (c_emot == 1) or (c_inst == 1):
        return MODE_C
    # UNSPECIFIED IN SOURCE MATH: the implication's guard is not enabled; no
    # routing is dictated and the case is left unhandled.
    return None


def routing_consequence_dialogue_off(c_dialog_off):
    """Construct: routing consequence (dialogue unavailability) — Section 3.11.
    Equation implemented:
        C_dialog|off(t) = 1
            =>  transitioning to Self-Alignment (Mode C)
                OR engaging the Interruption Handler
    """
    # c_dialog_off -> C_dialog|off(t) in {0, 1}
    if c_dialog_off == 1:
        return (Q_C_SELF, Q_INT)
    # UNSPECIFIED IN SOURCE MATH: the implication's guard is not enabled; no
    # routing is dictated and the case is left unhandled.
    return None


# =============================================================================
# Section 3.12 — Internal Regulatory Mechanics of the Modes
# =============================================================================

# ---- Section 3.12.1 — Sequential Arrangement of Components ----

# Construct: sequential component arrangement m = (c1, c2) — Section 3.12.1.
# Equation implemented:
#     FOR ALL m in {A, B, C} (and handlers):
#         m = ( c1^(m), c2^(m) ),  c1^(m) precedes c2^(m)
# with the concrete component pairs given by the source table.
SEQUENTIAL_COMPONENT_PAIRS = {
    "Mode A": (
        "Intended What (Clear Intention, Transactional Risk & Misinterpretation)",
        'External Providing "Why" (Contextual Grounding & Transaction Reduction)',
    ),
    "Mode B": (
        "Observed What",
        "Provisional Contextual Whys (Multiple Choice / Inquiry)",
    ),
    "Mode C (Self-Alignment)": (
        'Internal "Provisional Contextual Why"',
        "Observational Refinement (Temporal Distance)",
    ),
    "Mode C (Shared-Alignment)": (
        "Acknowledgment of Interpretive What and Observed What",
        "Provisional Contextual Whys (Inquiry)",
    ),
    "Stabilization Handler": (
        "Acknowledgment of Clarified What & Why (or Directly Articulated/Known What & Why)",
        "Proportional Forward Step (according to the Clarified/Known What & Why)",
    ),
    "Interruption Handler": (
        "Suspending the Interpretive Loop (Cognitive Offloading)",
        "Shift to Self-Alignment",
    ),
}


def mode_effect(phi_m, c1_m_t, c2_m_t):
    """Construct: working-mechanism composition — Section 3.12.1.
    Equation implemented:
        Effect^(m)(t) = Phi_m( c1^(m)(t), c2^(m)(t) )
    Phi_m denotes the sequential composition operator ("multiple empirically
    validated mechanisms may interact sequentially, with their combined
    regulatory effect depending on the order in which they are engaged"); its
    functional form is not specified in the source, so it is injected.
    """
    # phi_m  -> Phi_m: sequential composition operator (form not specified in the source)
    # c1_m_t -> c1^(m)(t): first component of mode m at t
    # c2_m_t -> c2^(m)(t): second component of mode m at t
    return phi_m(c1_m_t, c2_m_t)


# ---- Section 3.12.2 — The Dual-Regulatory Mechanism ----

# Construct: dual-regulatory scope-and-directionality domain D — Section 3.12.2.
# Equations implemented:
#     D = scope x directionality
#     scope = {intrapersonal, interpersonal},
#     directionality = {initiator, receiver}
#     |D| = 2 x 2 = 4 regulatory cells
SCOPE = ("intrapersonal", "interpersonal")
DIRECTIONALITY = ("initiator", "receiver")
DUAL_REGULATORY_DOMAIN = frozenset((scope, direction)
                                   for scope in SCOPE for direction in DIRECTIONALITY)


def effort_initiator(construct,
                     separating_the_operational_what_from_the_contextual_why,
                     selecting_the_appropriate_regulatory_mode,
                     navigating_potential_mode_transitions,
                     generating_contextual_provisional_why_hypotheses,
                     formulating_an_acknowledgment_and_proportional_forward_step):
    """Construct: Initiator-side executive-task effort — Section 3.12.2.
    Equation implemented:
        Effort_initiator(t) = construct( separating the Operational What from
            the Contextual Why, selecting the appropriate regulatory mode,
            navigating potential mode transitions, generating contextual
            Provisional Why hypotheses, and formulating an appropriate
            Acknowledgment and Proportional Forward Step )
    The source gives no functional form for construct(.); it is injected as a
    callable parameter and is NOT invented here.
    """
    # construct -> construct(.): effort construction operator (no functional form specified in the source)
    # separating_the_operational_what_from_the_contextual_why -> "separating the Operational What from the Contextual Why"
    # selecting_the_appropriate_regulatory_mode -> "selecting the appropriate regulatory mode"
    # navigating_potential_mode_transitions -> "navigating potential mode transitions"
    # generating_contextual_provisional_why_hypotheses -> "generating contextual Provisional Why hypotheses"
    # formulating_an_acknowledgment_and_proportional_forward_step -> "formulating an appropriate Acknowledgment and Proportional Forward Step"
    return construct(separating_the_operational_what_from_the_contextual_why,
                     selecting_the_appropriate_regulatory_mode,
                     navigating_potential_mode_transitions,
                     generating_contextual_provisional_why_hypotheses,
                     formulating_an_acknowledgment_and_proportional_forward_step)


def effort_initiator_hypothesis(effort_initiator_active, pfc_up, amygdala_down, ivp_down):
    """Construct: Initiator-side executive-task hypothesis — Section 3.12.2.
    Equation implemented (material implication; the source flags it as "a
    testable hypothesis awaiting direct empirical investigation"):
        Effort_initiator(t)  =>  PFC_initiator(t) up
                                 AND Amygdala_initiator(t) down
                                 AND IVP_initiator(t) down
    """
    # effort_initiator_active -> Effort_initiator(t) engaged
    # pfc_up        -> PFC_initiator(t) up (prefrontal regulatory engagement increases)
    # amygdala_down -> Amygdala_initiator(t) down (amygdala activation decreases)
    # ivp_down      -> IVP_initiator(t) down (Interpretive Velocity decreases)
    return (not effort_initiator_active) or (pfc_up and amygdala_down and ivp_down)


# ---- Section 3.12.3 — The Mechanics of the Interpretive Velocity Parameter ----

def friction_active(isolating_the_operational_what,
                    selecting_the_appropriate_regulatory_mode,
                    generating_contextual_provisional_why_hypotheses,
                    relying_on_self_alignment_observation):
    """Construct: friction active indicator — Section 3.12.3.
    Equation implemented:
        friction active(t) := 1[ isolating the Operational What
            OR selecting the appropriate regulatory mode
            OR generating contextual Provisional Why hypotheses
            OR relying on Self-Alignment observation, particularly in
               low-stakes environments during early stages of practice ]
    """
    # isolating_the_operational_what -> "isolating the Operational What" disjunct
    # selecting_the_appropriate_regulatory_mode -> "selecting the appropriate regulatory mode" disjunct
    # generating_contextual_provisional_why_hypotheses -> "generating contextual Provisional Why hypotheses" disjunct
    # relying_on_self_alignment_observation -> "relying on Self-Alignment observation, particularly in low-stakes environments during early stages of practice" disjunct
    return int(isolating_the_operational_what
               or selecting_the_appropriate_regulatory_mode
               or generating_contextual_provisional_why_hypotheses
               or relying_on_self_alignment_observation)


def friction_implication(friction_active_value, d_ivp_dt):
    """Construct: friction deceleration implication — Section 3.12.3.
    Equation implemented (material implication):
        friction active(t) = 1  =>  d IVP/dt < 0
    """
    # friction_active_value -> friction active(t) in {0, 1}
    # d_ivp_dt              -> d IVP/dt
    return (friction_active_value != 1) or (d_ivp_dt < 0)


def developmental_encoding_ivp(ivp_habituated, ivp_naive):
    """Construct: Developmental Encoding coupling — Section 3.12.3.
    Equation implemented:
        IVP_habituated(t) < IVP_naive(t)   as n_practice -> infinity
    (n_practice is the cumulative number of ELM-regulated interactions.)
    """
    # ivp_habituated -> IVP_habituated(t)
    # ivp_naive      -> IVP_naive(t)
    return ivp_habituated < ivp_naive


# ---- Section 3.12.4 — Contextual Sufficiency Criterion as an Observable
#      Behavioral Shift ----

def test_stab(acknowledgment, proportional_forward_step, ordered_combine, delta_reg):
    """Construct: Stabilization Handler behavioral test test_stab —
    Section 3.12.4.
    Equation implemented:
        test_stab(t) : ( Acknowledgment (+) Proportional Forward Step )(t)
                       -> Delta_regulatory(t)
    The test administers the combined pattern and maps it to the observed
    regulatory shift; the pair (administered combined pattern,
    Delta_regulatory(t)) is returned as the map's graph.
    """
    # acknowledgment            -> Acknowledgment (input to the combined pattern)
    # proportional_forward_step -> Proportional Forward Step (input to the combined pattern)
    # ordered_combine           -> (+): ordered/integrated combination operator
    # delta_reg                 -> Delta_regulatory(t): observed regulatory shift
    return (ordered_combine(acknowledgment, proportional_forward_step), delta_reg)


def test_stab_succeeds(delta_reg):
    """Construct: test_stab success biconditional — Section 3.12.4.
    Equation implemented:
        test_stab(t) succeeds  <=>  Delta_regulatory(t) > 0
    """
    # delta_reg -> Delta_regulatory(t)
    return delta_reg > 0


def csc_retrospective(delta_regulatory_approaching_from_above):
    """Construct: formal retrospective CSC criterion — Section 3.12.4.
    Equation implemented:
        CSC(t) = lim_{tau -> t+} 1[ Delta_regulatory(tau) > 0 ]
                 (retrospective)
    The right-limit of a {0,1}-valued indicator exists iff it is eventually
    constant approaching t from above; the value nearest t is returned.
    """
    # delta_regulatory_approaching_from_above -> Delta_regulatory(tau) samples ordered as tau -> t+
    indicators = [int(d > 0) for d in delta_regulatory_approaching_from_above]
    # UNSPECIFIED IN SOURCE MATH: behavior undefined for this case —
    # when the limit does not exist (indicator not eventually constant), the
    # source does not define CSC(t).
    return indicators[-1]


# ---- Section 3.12.5 — Internal System Architecture ----

# Construct: ELM_internal closed-loop pipeline — Section 3.12.5.
# Equation implemented:
#     ELM_internal :
#         Interpretive events  ->IVP->  [ Contextual Expression OR Contextual
#         Exploration OR Recursive Alignment ]  ->Stabilization Handler->
#         behavioral test  ->CSC->  { stabilization has been achieved OR
#         re-enters the regulatory routing process }
ELM_INTERNAL_PIPELINE = (
    "Interpretive events",
    "Interpretive Velocity Parameter",
    "[ Contextual Expression OR Contextual Exploration OR Recursive Alignment ]",
    "Stabilization Handler",
    "behavioral test",
    "Contextual Sufficiency Criterion",
    "{ stabilization has been achieved OR re-enters the regulatory routing process }",
)

# Construct: nested feedback-loop decomposition — Section 3.12.5.
# Equation implemented:
#     ELM = U_{k in {1,2,3}} F_k,   F_k subset F_{k+1}
#     F1 = behavioral stabilization, F2 = interpretive revision,
#     F3 = regulatory mode selection
F1_BEHAVIORAL_STABILIZATION = "behavioral stabilization"
F2_INTERPRETIVE_REVISION = "interpretive revision"
F3_REGULATORY_MODE_SELECTION = "regulatory mode selection"


def nested_feedback_nesting(F1, F2, F3):
    """Construct: nested feedback-loop nesting F_k subset F_{k+1} —
    Section 3.12.5.
    Equation implemented:
        F_1 subset F_2  AND  F_2 subset F_3
    (ELM = U_{k in {1,2,3}} F_k with F1 = behavioral stabilization,
    F2 = interpretive revision, F3 = regulatory mode selection.)
    """
    # F1 -> F_1 = behavioral stabilization (set)
    # F2 -> F_2 = interpretive revision (set)
    # F3 -> F_3 = regulatory mode selection (set)
    return (F1 < F2) and (F2 < F3)


# =============================================================================
# Section 4 — Neuroscientific Alignment (directional transfer function)
# =============================================================================

def elm_regulation_directional(elm_regulation_active, amygdala_down, pfc_up):
    """Construct: Neuroscientific Alignment qualitative transfer-function —
    Section 4.
    Equation implemented (material implication; the source states "This
    metabolic and neural account is presented as theoretically consistent
    ... without claiming direct neurobiological causation or mechanistic
    equivalence", and that the directional arrow "is the maximum
    formalization consistent with the text"):
        ELM-regulation(t)  =>  ( Amygdala(t) down  AND  PFC(t) up )
    """
    # elm_regulation_active -> ELM-regulation(t)
    # amygdala_down         -> Amygdala(t) down
    # pfc_up                -> PFC(t) up
    return (not elm_regulation_active) or (amygdala_down and pfc_up)


# =============================================================================
# Section 5 — Developmental Encoding and Longitudinal Stabilization
# =============================================================================

def latency_derivative_positive(d_t_latency_proportional_dn):
    """Construct: developmental-encoding latency derivative — Section 5.
    Equation implemented:
        d/dn  T_latency-proportional(n)  >  0
        (latency increases as the system deliberately waits for CSC)
    T_latency-proportional(n) is the latency between initial interpretive
    activation and proportional stabilization; n is the cumulative number of
    ELM-regulated interactions.
    """
    # d_t_latency_proportional_dn -> d/dn T_latency-proportional(n)
    return d_t_latency_proportional_dn > 0


def shift_time_derivative_negative(d_tau_shift_dn):
    """Construct: metabolic-shift efficiency derivative — Section 5.
    Equation implemented:
        d/dn  tau_shift(n)  <  0
        (metabolic shift occurs more efficiently/faster)
    tau_shift(n) is the time required for the metabolic shift from
    amygdala-driven reactivity to prefrontal evaluation.
    """
    # d_tau_shift_dn -> d/dn tau_shift(n)
    return d_tau_shift_dn < 0


def wait_for_csc_expectation_converges(wait_for_csc_limit):
    """Construct: wait-for-CSC expectation limit — Section 5.
    Equation implemented:
        E[ wait-for-CSC(n) ]  ->  1   as n -> infinity
    """
    # wait_for_csc_limit -> lim_{n -> infinity} E[ wait-for-CSC(n) ]
    return wait_for_csc_limit == 1


def pic_expectation_vanishes(pic_limit, wait_for_csc_limit):
    """Construct: longitudinal autonomic calibration — Section 5.
    Equation implemented:
        E[ PIC(n) ] -> 0  as n -> infinity   AND
        E[ wait-for-CSC(n) ] -> 1
    ("The individual does not become less emotionally responsive; rather,
    their autonomic threat-detection systems become adaptively calibrated to
    wait for the Contextual Sufficiency Criterion before stabilizing a
    reaction.")
    """
    # pic_limit         -> lim_{n -> infinity} E[ PIC(n) ]
    # wait_for_csc_limit -> lim_{n -> infinity} E[ wait-for-CSC(n) ]
    return (pic_limit == 0) and (wait_for_csc_limit == 1)


# =============================================================================
# Section 6.1 — Asynchronous Habituation (directional relation)
# =============================================================================

def async_modality_implication(delta_t_async, delta_t_sync, ivp_async, ivp_sync):
    """Construct: asynchronous habituation directional relation — Section 6.1.
    Equation implemented (material implication):
        Delta t_async > Delta t_sync   =>   IVP_async(t) < IVP_sync(t)
    """
    # delta_t_async -> Delta t_async: asynchronous stimulus-response gap
    # delta_t_sync  -> Delta t_sync: synchronous stimulus-response gap
    # ivp_async     -> IVP_async(t)
    # ivp_sync      -> IVP_sync(t)
    return (not (delta_t_async > delta_t_sync)) or (ivp_async < ivp_sync)


# =============================================================================
# Section 6.3 — Developmental Encoding and Skill Internalization
# =============================================================================

def stabilization_time_derivative_negative(d_t_stabilization_dn):
    """Construct: stabilization-time derivative — Section 6.3.
    Equation implemented:
        d T_stabilization(n) / dn  <  0
    ("Over time, the time required to reach proportional stabilization
    decreases — meaning the regulatory pathway becomes more efficient, as
    premature closure is simultaneously deferred.")
    """
    # d_t_stabilization_dn -> d T_stabilization(n) / dn
    return d_t_stabilization_dn < 0


def regulation_efficiency_precision_tradeoff(t_stab_decreasing, pic_expectation_decreasing,
                                              ivp_decreasing, interpretive_agility_preserved):
    """Construct: combined regulation-efficiency-precision tradeoff —
    Section 6.3.
    Equation implemented:
        T_stab(n) down  AND  E[ PIC(n) ] down  AND  IVP(n) down
        while preserving permanent interpretive agility
    """
    # t_stab_decreasing           -> T_stab(n) down
    # pic_expectation_decreasing  -> E[ PIC(n) ] down
    # ivp_decreasing              -> IVP(n) down
    # interpretive_agility_preserved -> "preserving permanent interpretive agility"
    return (t_stab_decreasing and pic_expectation_decreasing
            and ivp_decreasing and interpretive_agility_preserved)


# =============================================================================
# Section 8 — Boundary Conditions (precondition predicates)
# =============================================================================

def bc_minimal_cooperative_participation(kappa_coop, kappa_coop_min):
    """Construct: boundary condition (i) Minimal cooperative participation —
    Section 8.
    Equation implemented:
        kappa_coop(t) >= kappa_coop_min   required for Shared-Alignment
    """
    # kappa_coop     -> kappa_coop(t): cooperative participation level
    # kappa_coop_min -> kappa_coop_min (NOT numerically specified in the source)
    return kappa_coop >= kappa_coop_min


def bc_non_clinical_scope(clinical):
    """Construct: boundary condition (ii) Non-clinical scope — Section 8.
    Equation implemented:
        clinical(t) = 0   required for primary application
    """
    # clinical -> clinical(t) in {0,1}: severe psychological disorder / trauma / neurocognitive impairment indicator
    return clinical == 0


def bc_baseline_epistemic_humility(eta_humility, eta_humility_min):
    """Construct: boundary condition (iii) Baseline epistemic humility —
    Section 8.
    Equation implemented:
        eta_humility(t) >= eta_humility_min   required for mode operation
    """
    # eta_humility     -> eta_humility(t): epistemic humility level
    # eta_humility_min -> eta_humility_min (NOT numerically specified in the source)
    return eta_humility >= eta_humility_min


# Construct: boundary condition (iv) Non-normative-truth — Section 8.
# Equation implemented:
#     ELM targets CSC, NOT | Why(t) - Truth |
ELM_OPERATIONAL_TARGET = "CSC"


# =============================================================================
# Section 8.1.1 — Social and Interactional Constraints
# =============================================================================

def power_asymmetry_routing(power_asymmetry_severe):
    """Construct: Hierarchical Asymmetry and Power Dynamics constraint —
    Section 8.1.1.
    Equation implemented:
        Power Asymmetry(t) >> 0   =>   Mode(t) -> C
    ">> 0" (severe power asymmetry) is a qualitative relation in the source;
    whether it holds is supplied as an input.
    """
    # power_asymmetry_severe -> Power Asymmetry(t) >> 0
    if power_asymmetry_severe:
        return MODE_C
    # UNSPECIFIED IN SOURCE MATH: the guard is not enabled; no routing is
    # dictated and the case is left unhandled.
    return None


def mode_a_cultural_invariance(mode_a_patterns_across_cultural_contexts):
    """Construct: Neurobiological Universality vs. Cultural Adaptation
    constraint — Section 8.1.1.
    Equation implemented:
        FOR ALL Cultural Context:
            Mode A( Intended What (+) Contextual Why ) = Invariant
    """
    # mode_a_patterns_across_cultural_contexts -> Mode A(Intended What (+) Contextual Why) values per cultural context
    # UNSPECIFIED IN SOURCE MATH: behavior undefined for this case —
    # an empty set of cultural contexts is not covered by the universal
    # quantifier's written form.
    return len(set(mode_a_patterns_across_cultural_contexts)) == 1


def fabricated_context_rupture(inconsistencies_accumulate_over_time):
    """Construct: Deception and Fabricated Context constraint — Section 8.1.1.
    Equation implemented:
        Inconsistencies accumulate over time
            => Fabricated Coherence Ruptures
            => Return to Mode Selection Logic
    """
    # inconsistencies_accumulate_over_time -> "Inconsistencies accumulate over time"
    if inconsistencies_accumulate_over_time:
        return ("Fabricated Coherence Ruptures", "Return to Mode Selection Logic")
    # UNSPECIFIED IN SOURCE MATH: the guard is not enabled; the case is left
    # unhandled.
    return None


def permanent_dialogue_severance(delta_dialog_permanently_zero):
    """Construct: Permanent Dialogue Severance constraint — Section 8.1.1.
    Equation implemented:
        delta_dialog(t) -> 0 permanently
            => state(t) -> Interruption Handler -> Self-Alignment
    """
    # delta_dialog_permanently_zero -> "delta_dialog(t) -> 0 permanently"
    if delta_dialog_permanently_zero:
        return (Q_INT, Q_C_SELF)
    # UNSPECIFIED IN SOURCE MATH: the guard is not enabled; the case is left
    # unhandled.
    return None


def tone_mismatch(tone):
    """Construct: Acoustic Contradictions and Recursive Routing (The Tone
    Mismatch) constraint — Section 8.1.1.
    Equation implemented:
        Tone(t) in { hostile, sarcastic, aggressive }
            => Observed What(t) <- Tone(t)  AND  Mode(t) -> C
    """
    # tone -> Tone(t)
    if tone in {"hostile", "sarcastic", "aggressive"}:
        return {"observed_what": tone, "mode": MODE_C}
    # UNSPECIFIED IN SOURCE MATH: the guard is not enabled; the case is left
    # unhandled.
    return None


def semantic_mismatch(semantic_mismatch_indicator):
    """Construct: Semantic Mismatch and State Conflation (The Vocabulary
    Constraint) — Section 8.1.1.
    Equation implemented:
        Semantic Mismatch(t) = 1
            => Mode(t) -> C
               AND Require( Separate( Contextual Why, Observed What ) )
    """
    # semantic_mismatch_indicator -> Semantic Mismatch(t) in {0, 1}
    if semantic_mismatch_indicator == 1:
        return (MODE_C, "Require(Separate(Contextual Why, Observed What))")
    # UNSPECIFIED IN SOURCE MATH: the guard is not enabled; the case is left
    # unhandled.
    return None


# =============================================================================
# Section 8.1.2 — Cognitive and Neurobiological Constraints
# =============================================================================

def metabolic_depletion_routing(m_metabolic, m_crit):
    """Construct: Cognitive Thresholds and Metabolic Depletion constraint —
    Section 8.1.2.
    Equation implemented:
        M_metabolic(t) < M_crit   =>   Mode(t) <- Self-Alignment
    """
    # m_metabolic -> M_metabolic(t)
    # m_crit      -> M_crit (NOT numerically specified in the source)
    if m_metabolic < m_crit:
        return Q_C_SELF
    # UNSPECIFIED IN SOURCE MATH: the guard is not enabled; the case is left
    # unhandled.
    return None


def acute_threat_bypass(threat_is_acute_biological_survival):
    """Construct: Domain Specificity and Autonomic Bypass (The Acute Threat
    Protocol) — Section 8.1.2.
    Equation implemented:
        Threat(t) = Acute (Biological Survival)
            => ELM System <- Bypassed
    """
    # threat_is_acute_biological_survival -> Threat(t) = Acute (Biological Survival)
    if threat_is_acute_biological_survival:
        return "Bypassed"
    # UNSPECIFIED IN SOURCE MATH: the guard is not enabled; the case is left
    # unhandled.
    return None


def fawning_longitudinal_falsification(inconsistency_over_time):
    """Construct: Trauma Responses and Longitudinal Falsification (The
    "Fawning" Variable) — Section 8.1.2.
    Equation implemented:
        inconsistency( apparent compliance, actual alignment ) > 0 over time
            => Mode(t) -> C
    """
    # inconsistency_over_time -> inconsistency(apparent compliance, actual alignment) over time
    if inconsistency_over_time > 0:
        return MODE_C
    # UNSPECIFIED IN SOURCE MATH: the guard is not enabled; the case is left
    # unhandled.
    return None


def cognitive_triage(why_consistently_irrational_manipulative_or_structurally_incoherent):
    """Construct: Evolutionary Triage and the "Coherence Abort" Protocol —
    Section 8.1.2.
    Equation implemented:
        Why(t) in { irrational, manipulative, structurally incoherent }
        consistently
            => Cognitive Triage ( Terminate Loop )
    """
    # why_consistently_irrational_manipulative_or_structurally_incoherent -> "Why(t) in {irrational, manipulative, structurally incoherent} consistently"
    if why_consistently_irrational_manipulative_or_structurally_incoherent:
        return "Cognitive Triage (Terminate Loop)"
    # UNSPECIFIED IN SOURCE MATH: the guard is not enabled; the case is left
    # unhandled.
    return None


def working_memory_whys_constraint(n_provisional_whys, w_max):
    """Construct: Sequential Processing and Cognitive Load (The Overflow
    Defense) — Section 8.1.2.
    Equation implemented:
        | { Why_i } |  <=  W_max,   W_max in {1, 2} (typical)
    """
    # n_provisional_whys -> | { Why_i } |: number of simultaneous provisional explanations
    # w_max              -> W_max (constrained to "typically one or two"; no fixed value specified)
    return n_provisional_whys <= w_max


def alexithymia_routing(internal_state_labeling_failed):
    """Construct: Neurodivergence and Interoceptive Deficits (The Alexithymia
    Constraint) — Section 8.1.2.
    Equation implemented:
        Internal state labeling = failed
            => Self-Alignment unavailable  AND  Mode(t) in { B, Shared-C }
    """
    # internal_state_labeling_failed -> "Internal state labeling = failed"
    if internal_state_labeling_failed:
        return {"self_alignment_available": False, "mode": (MODE_B, "Shared-C")}
    # UNSPECIFIED IN SOURCE MATH: the guard is not enabled; the case is left
    # unhandled.
    return None


# =============================================================================
# Section 8.1.3 — Strategic and Adversarial Contexts
# =============================================================================

def weaponization_limit(actions_consistently_differ_from_stated_why, csc_value):
    """Construct: Stabilization vs. Coercion (The Weaponization Limit) —
    Section 8.1.3.
    Equation implemented:
        actions(t') != stated Why(t) consistently
            => CSC(t) ruptures,  Mode -> C
    """
    # actions_consistently_differ_from_stated_why -> actions(t') != stated Why(t) consistently
    # csc_value -> CSC(t) (ruptures when the guard fires)
    if actions_consistently_differ_from_stated_why:
        return ("CSC ruptures", MODE_C)
    # UNSPECIFIED IN SOURCE MATH: the guard is not enabled; the case is left
    # unhandled.
    return None


def verbal_hostility_routing(hostility_verbal):
    """Construct: Hostile Actors and Zero-Sum Environments constraint —
    Section 8.1.3.
    Equation implemented:
        Hostility_verbal(t) > 0   =>   Mode(t) -> C
    """
    # hostility_verbal -> Hostility_verbal(t)
    if hostility_verbal > 0:
        return MODE_C
    # UNSPECIFIED IN SOURCE MATH: the guard is not enabled; the case is left
    # unhandled.
    return None


def epistemic_denial_routing(observed_what_denied):
    """Construct: Epistemic Denial (The "Baseline Reality" Rupture) —
    Section 8.1.3.
    Equation implemented:
        Observed What(t) denied
            => Shared-Alignment aborts
            => Mode -> Self-Alignment
    """
    # observed_what_denied -> "Observed What(t) denied"
    if observed_what_denied:
        return ("Shared-Alignment aborts", Q_C_SELF)
    # UNSPECIFIED IN SOURCE MATH: the guard is not enabled; the case is left
    # unhandled.
    return None


# =============================================================================
# Section 8.1.4 — Implementation and Scaling Constraints
# =============================================================================

def f_hub(observed_whats, synthesize):
    """Construct: Multiagent Scaling and Central Node Routing (hub function)
    — Section 8.1.4.
    Equation implemented:
        f_hub : { W_1, W_2, ..., W_n }  ->  Y_unified
    The synthesis performed by the central regulating node has no specified
    functional form in the source; it is injected as a callable parameter.
    """
    # observed_whats -> {W_1, W_2, ..., W_n}: multiple Observed Whats from different participants
    # synthesize     -> the central node's synthesis operator (form not specified in the source)
    return synthesize(observed_whats)


def synthetic_sender_ivp_deceleration(sender_human_or_synthetic, mode_b_or_c_inquiry_valid,
                                       d_ivp_receiver_dt):
    """Construct: Synthetic Empathy and Human-Computer Interaction constraint
    — Section 8.1.4.
    Equation implemented (material implication):
        Sender in { human, synthetic }  AND  Mode B/C inquiry valid
            =>  d IVP_receiver / dt  <  0
    """
    # sender_human_or_synthetic -> Sender in {human, synthetic}
    # mode_b_or_c_inquiry_valid  -> Mode B/C inquiry valid
    # d_ivp_receiver_dt          -> d IVP_receiver/dt
    return (not (sender_human_or_synthetic and mode_b_or_c_inquiry_valid)) or (d_ivp_receiver_dt < 0)


def novice_overload_environment(structural_habit_unestablished):
    """Construct: The "Novice Overload" Paradox and Asynchronous Habituation
    constraint — Section 8.1.4.
    Equation implemented:
        Structural Habit(n) = Unestablished
            => Required Environment in { Asynchronous, Low-Stakes }
    """
    # structural_habit_unestablished -> Structural Habit(n) = Unestablished
    if structural_habit_unestablished:
        return ("Asynchronous", "Low-Stakes")
    # UNSPECIFIED IN SOURCE MATH: the guard is not enabled; the case is left
    # unhandled.
    return None


def initiator_priority(t_initiate_a, t_initiate_b):
    """Construct: Symmetrical Mastery and Sequential Turn-Allocation (The
    Initiator-Priority Principle) — Section 8.1.4.
    Equation implemented:
        t_initiate(A) < t_initiate(B)
            => A is initiator, B is responder
    """
    # t_initiate_a -> t_initiate(A)
    # t_initiate_b -> t_initiate(B)
    if t_initiate_a < t_initiate_b:
        return {"A": "initiator", "B": "responder"}
    # UNSPECIFIED IN SOURCE MATH: behavior undefined for this case —
    # role assignment when t_initiate(A) >= t_initiate(B) is not written in
    # the source; the case is left unhandled.


def no_deadlock_symmetrical_mastery(t_initiate_a, t_initiate_b):
    """Construct: deadlock non-existence under distinct initiation times —
    Section 8.1.4.
    Equation implemented:
        NOT-EXISTS deadlock  when  t_initiate(A) != t_initiate(B)
    """
    # t_initiate_a -> t_initiate(A)
    # t_initiate_b -> t_initiate(B)
    if t_initiate_a != t_initiate_b:
        return True  # no deadlock exists
    # UNSPECIFIED IN SOURCE MATH: behavior undefined for this case —
    # deadlock status when t_initiate(A) = t_initiate(B) is not written in
    # the source; the case is left unhandled.


# =============================================================================
# Section 11.4.1 — Phased Empirical Testing and Hypotheses (H1-H15)
# Each hypothesis is translated as a predicate over the expectation values
# that appear in it; the expectation operator E[.] itself is not instantiated
# anywhere (the source does not specify an estimator).
# =============================================================================

# Construct: ELM component set C_ELM — Section 11.4.1 (H1).
C_ELM = frozenset({
    "Operational What separation",
    "types of Operational What",
    "single Provisional Why",
    "multiple Provisional Why",
    "Proportional Forward Step",
    "Internal Provisional Why",
    "External Contextual Why",
    "Acknowledgment of Interpretive/Observed What",
    "Observational Refinement",
    "Acknowledgment of Clarified What & Why",
})


def h1_component_isolation(pfc_activity_expectations, pfc_activity_expectation_baseline,
                            hrv_expectations, hrv_expectation_baseline):
    """Construct: H1 (Component Isolation) — Section 11.4.1, Phase I.
    Equation implemented:
        FOR ALL c in C_ELM:
            E[ PFC_activity(c) ] > E[ PFC_activity(baseline) ]
            AND  E[ HRV(c) ] > E[ HRV(baseline) ]
    """
    # pfc_activity_expectations           -> E[ PFC_activity(c) ] keyed by c in C_ELM
    # pfc_activity_expectation_baseline   -> E[ PFC_activity(baseline) ]
    # hrv_expectations                    -> E[ HRV(c) ] keyed by c in C_ELM
    # hrv_expectation_baseline            -> E[ HRV(baseline) ]
    return (all(pfc_activity_expectations[c] > pfc_activity_expectation_baseline for c in C_ELM)
            and all(hrv_expectations[c] > hrv_expectation_baseline for c in C_ELM))


def h2_intra_mode_synthesis(reg_eff_expectations, reg_eff_expectation_unregulated):
    """Construct: H2 (Intra-Mode Synthesis) — Section 11.4.1, Phase I.
    Equation implemented:
        FOR ALL m in {A, B, C}:
            E[ RegEff(m) ] > E[ RegEff(unregulated) ]
    (RegEff is metabolic-and-autonomic regulatory efficiency.)
    """
    # reg_eff_expectations              -> E[ RegEff(m) ] keyed by m in {A, B, C}
    # reg_eff_expectation_unregulated   -> E[ RegEff(unregulated) ]
    return all(reg_eff_expectations[m] > reg_eff_expectation_unregulated
               for m in (MODE_A, MODE_B, MODE_C))


def h3_csc(csc_value, autonomic_expectation, baseline):
    """Construct: H3 (Contextual Sufficiency Criterion) — Section 11.4.1,
    Phase I.
    Equation implemented (implication pair):
        CSC(t) = 1  =>  E[ Autonomic(t + tau) ] -> baseline
        CSC(t) = 0  =>  E[ Autonomic(t + tau) ] > baseline
    """
    # csc_value             -> CSC(t) in {0, 1}
    # autonomic_expectation -> E[ Autonomic(t + tau) ]
    # baseline              -> baseline autonomic activity
    return ((csc_value != 1) or (autonomic_expectation == baseline)) and \
           ((csc_value != 0) or (autonomic_expectation > baseline))


def h4_cognitive_offloading(zeigarnik_persistence_expectation_ih,
                            zeigarnik_persistence_expectation_unsupported,
                            tau_recovery_expectation_ih,
                            tau_recovery_expectation_unsupported):
    """Construct: H4 (Cognitive Offloading via Interruption Handler) —
    Section 11.4.1, Phase I.
    Equation implemented:
        E[ Zeigarnik persistence(IH) ] < E[ Zeigarnik persistence(unsupported) ]
        AND  E[ tau_recovery(IH) ] < E[ tau_recovery(unsupported) ]
    """
    # zeigarnik_persistence_expectation_ih           -> E[ Zeigarnik persistence(IH) ]
    # zeigarnik_persistence_expectation_unsupported  -> E[ Zeigarnik persistence(unsupported) ]
    # tau_recovery_expectation_ih                    -> E[ tau_recovery(IH) ]
    # tau_recovery_expectation_unsupported           -> E[ tau_recovery(unsupported) ]
    return ((zeigarnik_persistence_expectation_ih < zeigarnik_persistence_expectation_unsupported)
            and (tau_recovery_expectation_ih < tau_recovery_expectation_unsupported))


def h5_neural_coupling(inc_expectation_elm, inc_expectation_unregulated):
    """Construct: H5 (Neural Coupling) — Section 11.4.1, Phase I.
    Equation implemented:
        E[ INC_ELM ] > E[ INC_unregulated ]
    (INC = interpersonal neural coupling measured via dual-fMRI or fNIRS
    hyperscanning.)
    """
    # inc_expectation_elm          -> E[ INC_ELM ]
    # inc_expectation_unregulated  -> E[ INC_unregulated ]
    return inc_expectation_elm > inc_expectation_unregulated


def h6_system_level_integration(full_elm_execution, ivp_modulated,
                                sigma_interpretive_response_moderate):
    """Construct: H6 (System-Level Integration) — Section 11.4.1, Phase I.
    Equation implemented (material implication):
        Full-ELM execution  =>  ( IVP modulated
                                  AND sigma(interpretive response) moderate
                                  across shifting conditions )
    """
    # full_elm_execution                  -> Full-ELM execution
    # ivp_modulated                       -> IVP modulated
    # sigma_interpretive_response_moderate -> sigma(interpretive response) moderate across shifting conditions
    return (not full_elm_execution) or (ivp_modulated and sigma_interpretive_response_moderate)


def h7_pediatric_adolescent_acquisition(elm_internalization_expectation_derivatives):
    """Construct: H7 (Pediatric/Adolescent Acquisition) — Section 11.4.1,
    Phase II.
    Equation implemented:
        FOR ALL a in { children, adolescents }:
            d/dt E[ ELM-internalization(a, t) ]  >  0
    """
    # elm_internalization_expectation_derivatives -> d/dt E[ ELM-internalization(a, t) ] keyed by a in {children, adolescents}
    return all(d > 0 for d in elm_internalization_expectation_derivatives.values())


def h8_adult_acquisition(d_pfc_activation_load_dn, d_tau_mode_selection_dn,
                         d_error_mode_selection_dn):
    """Construct: H8 (Adult Acquisition) — Section 11.4.1, Phase II.
    Equation implemented:
        d/dn E[ PFC activation load(n) ] < 0
        AND  d/dn E[ tau_mode-selection(n) ] < 0
        AND  d/dn E[ error_mode-selection(n) ] < 0
    """
    # d_pfc_activation_load_dn  -> d/dn E[ PFC activation load(n) ]
    # d_tau_mode_selection_dn   -> d/dn E[ tau_mode-selection(n) ]
    # d_error_mode_selection_dn -> d/dn E[ error_mode-selection(n) ]
    return ((d_pfc_activation_load_dn < 0)
            and (d_tau_mode_selection_dn < 0)
            and (d_error_mode_selection_dn < 0))


def h9_ivp_modulation(ivp_expectation_elm, ivp_expectation_control,
                      pic_expectation_elm, pic_expectation_control):
    """Construct: H9 (IVP Modulation) — Section 11.4.1, Phase II.
    Equation implemented:
        E[ IVP_ELM ] < E[ IVP_control ]
        AND  E[ PIC_ELM ] < E[ PIC_control ]
    """
    # ivp_expectation_elm     -> E[ IVP_ELM ]
    # ivp_expectation_control -> E[ IVP_control ]
    # pic_expectation_elm     -> E[ PIC_ELM ]
    # pic_expectation_control -> E[ PIC_control ]
    return ((ivp_expectation_elm < ivp_expectation_control)
            and (pic_expectation_elm < pic_expectation_control))


def h10_relational_familiarity_generation(rho_expectation_after_mode_b,
                                          rho_expectation_unregulated):
    """Construct: H10 (Relational Familiarity Generation) — Section 11.4.1,
    Phase III.
    Equation implemented:
        E[ rho_after Mode B ] > E[ rho_unregulated ]
    """
    # rho_expectation_after_mode_b -> E[ rho_after Mode B ]
    # rho_expectation_unregulated  -> E[ rho_unregulated ]
    return rho_expectation_after_mode_b > rho_expectation_unregulated


def h11_institutional_performance(collab_performance_expectation_elm_org,
                                  collab_performance_expectation_control,
                                  conflict_escalation_expectation_elm_org,
                                  conflict_escalation_expectation_control):
    """Construct: H11 (Institutional Performance) — Section 11.4.1, Phase III.
    Equation implemented:
        E[ collab-performance_ELM-org ] > E[ collab-performance_control ]
        AND  E[ conflict-escalation_ELM-org ] < E[ conflict-escalation_control ]
    """
    # collab_performance_expectation_elm_org     -> E[ collab-performance_ELM-org ]
    # collab_performance_expectation_control     -> E[ collab-performance_control ]
    # conflict_escalation_expectation_elm_org    -> E[ conflict-escalation_ELM-org ]
    # conflict_escalation_expectation_control    -> E[ conflict-escalation_control ]
    return ((collab_performance_expectation_elm_org > collab_performance_expectation_control)
            and (conflict_escalation_expectation_elm_org < conflict_escalation_expectation_control))


def h12_economic_systemic_impact(cognitive_inefficiency_expectation_elm,
                                 cognitive_inefficiency_expectation_control,
                                 temporal_inefficiency_expectation_elm,
                                 temporal_inefficiency_expectation_control):
    """Construct: H12 (Economic/Systemic Impact) — Section 11.4.1, Phase III.
    Equation implemented:
        E[ cognitive inefficiency_ELM ] < E[ cognitive inefficiency_control ]
        AND  E[ temporal inefficiency_ELM ] < E[ temporal inefficiency_control ]
    """
    # cognitive_inefficiency_expectation_elm     -> E[ cognitive inefficiency_ELM ]
    # cognitive_inefficiency_expectation_control -> E[ cognitive inefficiency_control ]
    # temporal_inefficiency_expectation_elm      -> E[ temporal inefficiency_ELM ]
    # temporal_inefficiency_expectation_control  -> E[ temporal inefficiency_control ]
    return ((cognitive_inefficiency_expectation_elm < cognitive_inefficiency_expectation_control)
            and (temporal_inefficiency_expectation_elm < temporal_inefficiency_expectation_control))


def h13_relational_stability(pic_incidence_expectation_elm,
                             pic_incidence_expectation_control,
                             cyclical_escalation_expectation_elm,
                             cyclical_escalation_expectation_control):
    """Construct: H13 (Relational Stability) — Section 11.4.1, Phase III.
    Equation implemented:
        E[ PIC incidence_ELM(t) ] < E[ PIC incidence_control(t) ]
        AND  E[ cyclical-escalation_ELM ] < E[ cyclical-escalation_control ]
    """
    # pic_incidence_expectation_elm           -> E[ PIC incidence_ELM(t) ]
    # pic_incidence_expectation_control       -> E[ PIC incidence_control(t) ]
    # cyclical_escalation_expectation_elm     -> E[ cyclical-escalation_ELM ]
    # cyclical_escalation_expectation_control -> E[ cyclical-escalation_control ]
    return ((pic_incidence_expectation_elm < pic_incidence_expectation_control)
            and (cyclical_escalation_expectation_elm < cyclical_escalation_expectation_control))


def h14_longitudinal_identity_shift(t1, t2,
                                    reflective_functioning_expectation_t1,
                                    reflective_functioning_expectation_t2,
                                    tau_reg_response_expectation_t1,
                                    tau_reg_response_expectation_t2):
    """Construct: H14 (Longitudinal Identity Shift) — Section 11.4.1,
    Phase III.
    Equation implemented:
        EXISTS t_1 < t_2 :
            E[ reflective-functioning(t_2) ] / E[ reflective-functioning(t_1) ] > 1
            AND  E[ tau_reg-response(t_2) ] / E[ tau_reg-response(t_1) ] != 1
    The existential quantifier is checked for the supplied pair (t_1, t_2).
    """
    # t1                                  -> t_1
    # t2                                  -> t_2
    # reflective_functioning_expectation_t1 -> E[ reflective-functioning(t_1) ]
    # reflective_functioning_expectation_t2 -> E[ reflective-functioning(t_2) ]
    # tau_reg_response_expectation_t1     -> E[ tau_reg-response(t_1) ]
    # tau_reg_response_expectation_t2     -> E[ tau_reg-response(t_2) ]
    return ((t1 < t2)
            and ((reflective_functioning_expectation_t2 / reflective_functioning_expectation_t1) > 1)
            and ((tau_reg_response_expectation_t2 / tau_reg_response_expectation_t1) != 1))


def h15_strategic_deception_constraint(d_coherence_dt_given_deceptive_why):
    """Construct: H15 (Strategic Deception Constraint) — Section 11.4.1,
    Phase IV.
    Equation implemented:
        d/dt E[ coherence(t) | deceptive Why ]  <  0
    """
    # d_coherence_dt_given_deceptive_why -> d/dt E[ coherence(t) | deceptive Why ]
    return d_coherence_dt_given_deceptive_why < 0


# =============================================================================
# Appendix — Preliminary Operationalization of IVP and PIC
# =============================================================================

def f_affect_interrupt(T, elm_mode_engaged_to_defer_interpretation_pending_context):
    """Construct: f_affect-interrupt — Appendix.
    Equation implemented:
        f_affect-interrupt = | { t in T :
            ELM mode engaged to defer interpretation pending context } |
    """
    # T -> T: the observation interval
    # elm_mode_engaged_to_defer_interpretation_pending_context -> predicate "ELM mode engaged to defer interpretation pending context" on t in T
    return len({t for t in T if elm_mode_engaged_to_defer_interpretation_pending_context(t)})


def tau_why_maintained(t_resolution_minus_t_why_generation, expectation):
    """Construct: tau_why-maintained — Appendix.
    Equation implemented:
        tau_why-maintained = E[ t_resolution - t_why-generation ]
    The expectation operator's estimator is not specified in the source, so
    E[.] is injected as a callable parameter and is NOT instantiated here.
    """
    # t_resolution_minus_t_why_generation -> t_resolution - t_why-generation observations
    # expectation                          -> E[.]: expectation operator (estimator not specified in the source)
    return expectation(t_resolution_minus_t_why_generation)


def ivp_proxy(f_affect_interrupt_value, tau_why_maintained_value):
    """Construct: IVP_proxy — Appendix.
    Equation implemented:
        IVP_proxy = ( f_affect-interrupt, tau_why-maintained )
    """
    # f_affect_interrupt_value  -> f_affect-interrupt
    # tau_why_maintained_value  -> tau_why-maintained
    return (f_affect_interrupt_value, tau_why_maintained_value)


def pic_proxy_reduction(pic_proxy_decreasing, f_affect_interrupt_increasing,
                        tau_why_maintained_increasing):
    """Construct: PIC reduction proxy — Appendix.
    Equation implemented (biconditional):
        PIC_proxy down   <=>   f_affect-interrupt up
                               AND  tau_why-maintained up
    """
    # pic_proxy_decreasing          -> PIC_proxy down
    # f_affect_interrupt_increasing -> f_affect-interrupt up
    # tau_why_maintained_increasing -> tau_why-maintained up
    return pic_proxy_decreasing == (f_affect_interrupt_increasing and tau_why_maintained_increasing)


# =============================================================================
# NOT IMPLEMENTED — constructs flagged UNFORMALIZABLE AS WRITTEN in the source
# (no equation exists to translate; implementing them would require inventing
# logic not present in the source's own audit classification)
# =============================================================================

_NOT_IMPLEMENTED_MSG = ("no VERIFIED equation exists to translate; implementing this "
                        "would require inventing logic not present in the audited "
                        "formalization")

NOT_IMPLEMENTED = {
    "Introduction narrative (Section 1)": _NOT_IMPLEMENTED_MSG,
    "Meaning-Making Under Uncertainty (Section 2.2)": _NOT_IMPLEMENTED_MSG,
    "Provisional Contextual Attribution and Epistemic Humility (Section 2.3)": _NOT_IMPLEMENTED_MSG,
    "Interpretive Coherence qualitative narrative (Section 2.4 narrative; equations ARE implemented)": _NOT_IMPLEMENTED_MSG,
    "ELM Formal Definition qualitative narrative (Section 3.1 narrative; tuple and objective ARE implemented)": _NOT_IMPLEMENTED_MSG,
    "Operational Structure qualitative narrative (Section 3.2 narrative; FSM IS implemented)": _NOT_IMPLEMENTED_MSG,
    "Cognitive Architectures & Predictive Processing narrative (Section 3.12.1)": _NOT_IMPLEMENTED_MSG,
    "Working-Mechanism narrative text blocks (Section 3.12.1; the component-pair table and Effect composition ARE implemented)": _NOT_IMPLEMENTED_MSG,
    "Dual-Regulatory theoretical and neurobiological narrative (Section 3.12.2; the axes, |D|=4, and Effort equations ARE implemented)": _NOT_IMPLEMENTED_MSG,
    "IVP theoretical and predictive-processing narrative (Section 3.12.3; friction and habituation equations ARE implemented)": _NOT_IMPLEMENTED_MSG,
    "Developmental Encoding and precision-weighting narrative (Section 3.12.3)": _NOT_IMPLEMENTED_MSG,
    "CSC introductory theoretical narrative (Section 3.12.4; the behavioral test IS implemented)": _NOT_IMPLEMENTED_MSG,
    "Feedback-monitoring concluding narrative (Section 3.12.4)": _NOT_IMPLEMENTED_MSG,
    "Internal architecture figure notes and synthesis narrative (Section 3.12.5; the pipeline and nesting ARE implemented)": _NOT_IMPLEMENTED_MSG,
    "Figure 1 (Section 3.10) and Figure 2 (Section 3.12.5) as graphics": _NOT_IMPLEMENTED_MSG,
    "Neuroscientific Alignment precise mechanism (Section 4; only the directional transfer-function IS implemented)": _NOT_IMPLEMENTED_MSG,
    "Narrative neuroscience and neural-coupling context (Section 4)": _NOT_IMPLEMENTED_MSG,
    "Developmental Encoding theoretical narratives (Section 5; the four equations ARE implemented)": _NOT_IMPLEMENTED_MSG,
    "Training and Implementation narrative (Section 6 intro; Section 6.2; Section 6.3 narrative)": _NOT_IMPLEMENTED_MSG,
    "Illustrative Applications (Section 7)": _NOT_IMPLEMENTED_MSG,
    "Boundary-conditions narrative (Section 8 intro and per-constraint narratives; the boundary-condition equations ARE implemented)": _NOT_IMPLEMENTED_MSG,
    "Summary of Boundary Conditions and Limitations (Section 8.2)": _NOT_IMPLEMENTED_MSG,
    "Theoretical Contributions (Section 9; cross-reference table only, no new constructs)": _NOT_IMPLEMENTED_MSG,
    "Theoretical Integration and Citation Framework (Section 10)": _NOT_IMPLEMENTED_MSG,
    "Practical Implications (Section 11.1)": _NOT_IMPLEMENTED_MSG,
    "Theoretical Implications (Section 11.2)": _NOT_IMPLEMENTED_MSG,
    "Empirical Grounding mechanism list (Section 11.3)": _NOT_IMPLEMENTED_MSG,
    "Directions for Future Research narratives (Section 11.4; hypotheses H1-H15 ARE implemented)": _NOT_IMPLEMENTED_MSG,
    "Conclusion (Section 12)": _NOT_IMPLEMENTED_MSG,
    "Declarations and Disclosures (Section 13)": _NOT_IMPLEMENTED_MSG,
    "References": _NOT_IMPLEMENTED_MSG,
    "Appendix qualitative narrative (the proxy equations ARE implemented)": _NOT_IMPLEMENTED_MSG,
}

# Appendices ("Full-Stack Turing Deadlock", "Dark Horizon", "Event
# Horizon", Multi-Agent Simulation, "Nightmare Mode", "Malicious Actor",
# "Omnicrisis", "Double-Bind", "Semantic Asymmetry", "Degraded Medium",
# "Byzantine Omnicrisis", Quick Reference Guide): SKIPPED — excluded from
# formalization per the source document's own scope constraint ("contain
# internal stress-testing prompts and summary reference materials, not ELM
# theoretical-architecture constructs").
APPENDICES_STATUS = "SKIPPED (excluded per source scope constraint)"


# =============================================================================
# COVERAGE REGISTRY — construct -> implementing symbol (for at-a-glance
# completeness checking; mirrors the Coverage Table in the delivery report)
# =============================================================================

CONSTRUCT_COVERAGE = {
    # Section 2.1
    "IVP(t) definition (2.1)": "ivp",
    "PIC(t) indicator (2.1)": "pic",
    "PIC sufficient-condition implication (2.1)": "pic_sufficient_condition_implication",
    # Section 2.4
    "A_What-Why(t) alignment (2.4)": "a_what_why_alignment",
    "Delta_regulatory(t) (2.4)": "delta_regulatory",
    "CSC(t) indicator (2.4 / 3.12.4)": "csc",
    # Section 3.1
    "ELM system tuple (3.1)": "ELMSystem",
    "Control objective (3.1)": "control_objective",
    # Section 3.2
    "ELM-FSM tuple (3.2)": "ELMFSM / elm_fsm / delta / ContextualSignal / Q_STATES",
    # Section 3.3
    "Mode Selection Logic (3.3)": "mode_selection",
    "A->C guard (3.3)": "a_to_c_guard",
    "B->C guard (3.3)": "b_to_c_guard",
    "Mode-C-subform (3.3)": "mode_c_subform",
    # Section 3.4
    "Event universe E (3.4)": "EVENT_UNIVERSE",
    "Triggering relation e -> IVP(t_0) (3.4)": "event_triggers_initial_ivp",
    # Section 3.5
    "What(t) typing/binding (3.5)": "what_binding",
    "Operational What(t) (3.5)": "OPERATIONAL_WHAT",
    # Section 3.6
    "RMC(t) indicator (3.6)": "rmc",
    "RMC consequence (3.6)": "rmc_consequence",
    # Section 3.7
    "enter_A guard (3.7.1)": "enter_A",
    "A->Stabilization (3.7.1)": "a_to_stabilization",
    "A->C (3.7.1)": "a_to_c",
    "enter_B guard (3.7.2)": "enter_B",
    "B->A (3.7.2)": "b_to_a",
    "B->Stabilization (3.7.2)": "b_to_stabilization",
    "B->C (3.7.2)": "b_to_c",
    "B->Interruption (3.7.2)": "b_to_interruption",
    "Mode-B-operable implication (3.7.2)": "mode_b_operable",
    "enter_C guard (3.7.3)": "enter_C",
    "Mode-C-branch (3.7.3)": "mode_c_branch",
    "Self-Alignment termination (3.7.3.1)": "self_alignment_termination",
    "Self-Alignment escalation (3.7.3.1)": "self_alignment_escalation",
    "Shared-Alignment bounded recursive loop (3.7.3.2)": "shared_alignment_loop",
    "Shared-Alignment bypass (3.7.3.2)": "shared_alignment_bypass",
    "Shared-Alignment interruption (3.7.3.2)": "shared_alignment_interruption",
    "Recursive Alignment Continuity (3.7.3.3)": "recursive_alignment_continues / RECURSIVE_ALIGNMENT_CONTAINMENT",
    "Stab->Closure (3.7.4)": "stab_to_closure",
    "Stab->{B,C} (3.7.4)": "stab_to_b_or_c",
    "Stab self-loop guard (3.7.4)": "stab_self_loop",
    "Interruption on dialog 1->0 (3.7.5)": "interruption_on_dialog_drop",
    "Interruption on dialog 0->1 (3.7.5)": "interruption_on_dialog_resume",
    "S(t) state tuple (3.7.6)": "s_t",
    "Cumulative context invariant (3.7.6)": "cumulative_context_invariant",
    # Section 3.8
    "Operational flows (3.8.1-3.8.5)": "OPERATIONAL_FLOW_* constants",
    "Pattern_A (3.8.1)": "pattern_a",
    "Pattern_B (3.8.2)": "pattern_b",
    "Pattern_C_self (3.8.3)": "pattern_c_self",
    "Pattern_C_shared (3.8.3)": "pattern_c_shared",
    "Pattern_Stab_Relational (3.8.4)": "pattern_stab_relational",
    "Pattern_Stab_Testing (3.8.4)": "pattern_stab_testing",
    "Pattern_Int (3.8.5)": "pattern_int",
    # Section 3.9
    "Layer set L_ELM (3.9)": "ELM_LAYERS",
    "Grounding constraint Sigma_grounding (3.9)": "sigma_grounding_constraint",
    # Section 3.10
    "ELM system-property statement (3.10)": "ELM_SYSTEM_PROPERTIES",
    "Termination guarantee (3.10)": "termination_guarantee",
    # Section 3.11
    "C_insuff (3.11)": "c_insufficient_context",
    "C_unfam (3.11)": "c_relational_unfamiliarity",
    "C_dist (3.11)": "c_interpretive_distortion",
    "C_emot (3.11)": "c_emotional_activation",
    "C_inst (3.11)": "c_relational_instability",
    "C_dialog|off (3.11)": "c_dialogue_unavailability",
    "Coupling rule (3.11)": "coupling_rule",
    "Routing consequence: unfamiliarity (3.11)": "routing_consequence_unfamiliarity",
    "Routing consequence: alignment (3.11)": "routing_consequence_alignment",
    "Routing consequence: dialogue off (3.11)": "routing_consequence_dialogue_off",
    # Section 3.12
    "Sequential component pairs (3.12.1)": "SEQUENTIAL_COMPONENT_PAIRS",
    "Effect^(m) = Phi_m(c1, c2) (3.12.1)": "mode_effect",
    "D = scope x directionality, |D| = 4 (3.12.2)": "SCOPE / DIRECTIONALITY / DUAL_REGULATORY_DOMAIN",
    "Effort_initiator construct (3.12.2)": "effort_initiator",
    "Effort_initiator hypothesis (3.12.2)": "effort_initiator_hypothesis",
    "friction active indicator (3.12.3)": "friction_active",
    "friction -> dIVP/dt < 0 implication (3.12.3)": "friction_implication",
    "IVP_habituated < IVP_naive (3.12.3)": "developmental_encoding_ivp",
    "test_stab map (3.12.4)": "test_stab",
    "test_stab succeeds biconditional (3.12.4)": "test_stab_succeeds",
    "CSC retrospective limit (3.12.4)": "csc_retrospective",
    "ELM_internal pipeline (3.12.5)": "ELM_INTERNAL_PIPELINE",
    "Nested feedback F1<F2<F3 (3.12.5)": "nested_feedback_nesting / F1_..F3_ constants",
    # Sections 4-6
    "ELM-regulation => (Amygdala down AND PFC up) (4)": "elm_regulation_directional",
    "d/dn T_latency > 0 (5)": "latency_derivative_positive",
    "d/dn tau_shift < 0 (5)": "shift_time_derivative_negative",
    "E[wait-for-CSC] -> 1 (5)": "wait_for_csc_expectation_converges",
    "E[PIC(n)] -> 0 AND E[wait] -> 1 (5)": "pic_expectation_vanishes",
    "async gap => IVP_async < IVP_sync (6.1)": "async_modality_implication",
    "d T_stabilization/dn < 0 (6.3)": "stabilization_time_derivative_negative",
    "Regulation-efficiency-precision tradeoff (6.3)": "regulation_efficiency_precision_tradeoff",
    # Section 8
    "BC (i) minimal cooperation (8)": "bc_minimal_cooperative_participation",
    "BC (ii) non-clinical scope (8)": "bc_non_clinical_scope",
    "BC (iii) epistemic humility (8)": "bc_baseline_epistemic_humility",
    "BC (iv) non-normative truth (8)": "ELM_OPERATIONAL_TARGET",
    "Power asymmetry => Mode C (8.1.1)": "power_asymmetry_routing",
    "Mode A cultural invariance (8.1.1)": "mode_a_cultural_invariance",
    "Deception rupture chain (8.1.1)": "fabricated_context_rupture",
    "Permanent severance (8.1.1)": "permanent_dialogue_severance",
    "Tone mismatch (8.1.1)": "tone_mismatch",
    "Semantic mismatch (8.1.1)": "semantic_mismatch",
    "Metabolic depletion => Self-Alignment (8.1.2)": "metabolic_depletion_routing",
    "Acute threat bypass (8.1.2)": "acute_threat_bypass",
    "Fawning longitudinal falsification (8.1.2)": "fawning_longitudinal_falsification",
    "Cognitive triage (8.1.2)": "cognitive_triage",
    "|{Why_i}| <= W_max (8.1.2)": "working_memory_whys_constraint",
    "Alexithymia routing (8.1.2)": "alexithymia_routing",
    "Weaponization limit (8.1.3)": "weaponization_limit",
    "Verbal hostility => Mode C (8.1.3)": "verbal_hostility_routing",
    "Epistemic denial => Self-Alignment (8.1.3)": "epistemic_denial_routing",
    "f_hub (8.1.4)": "f_hub",
    "Synthetic sender IVP deceleration (8.1.4)": "synthetic_sender_ivp_deceleration",
    "Novice overload environment (8.1.4)": "novice_overload_environment",
    "Initiator priority (8.1.4)": "initiator_priority",
    "No deadlock when t_A != t_B (8.1.4)": "no_deadlock_symmetrical_mastery",
    # Section 11.4.1
    "H1 (11.4.1)": "h1_component_isolation / C_ELM",
    "H2 (11.4.1)": "h2_intra_mode_synthesis",
    "H3 (11.4.1)": "h3_csc",
    "H4 (11.4.1)": "h4_cognitive_offloading",
    "H5 (11.4.1)": "h5_neural_coupling",
    "H6 (11.4.1)": "h6_system_level_integration",
    "H7 (11.4.1)": "h7_pediatric_adolescent_acquisition",
    "H8 (11.4.1)": "h8_adult_acquisition",
    "H9 (11.4.1)": "h9_ivp_modulation",
    "H10 (11.4.1)": "h10_relational_familiarity_generation",
    "H11 (11.4.1)": "h11_institutional_performance",
    "H12 (11.4.1)": "h12_economic_systemic_impact",
    "H13 (11.4.1)": "h13_relational_stability",
    "H14 (11.4.1)": "h14_longitudinal_identity_shift",
    "H15 (11.4.1)": "h15_strategic_deception_constraint",
    # Appendix
    "f_affect-interrupt (Appendix)": "f_affect_interrupt",
    "tau_why-maintained (Appendix)": "tau_why_maintained",
    "IVP_proxy (Appendix)": "ivp_proxy",
    "PIC_proxy biconditional (Appendix)": "pic_proxy_reduction",
}


# =============================================================================
# ELM COMPUTATIONAL LIBRARY CODE ENDS HERE. **WARNING**: The code above constitutes 
# the ELM Computational Library. Modifying the library code may alter the 
# Execution Logic of the Empathic Logic Model (ELM) Finite State Machine (FSM). 
# To execute or use this library, proceed to the bottom of this file, where the 
# headline titled "Execution and Implementation Area Begins Here" is provided. 
# Application-specific execution code, integration code, or other code intended 
# to use the ELM library should be added only below that headline.
# =============================================================================

"""
#############################################
EXECUTION AND IMPLEMENTATION AREA BEGINS HERE
#############################################
"""


# MOCK EXECUTION CODE.............

# =============================================================================
# MULTI-AGENT INTERACTION SIMULATION
# Scenario: High-Emotion Miscommunication -> Collaborative Resolution
# =============================================================================

def create_signal(kappa=1.0, rho=1.0, epsilon=0.0, delta_dist=0.0, iota=0.0,
                  delta_dialog=1, i_avail=1.0, i_req=0.5, receiver_response="acceptance",
                  instability=False, requires_articulation=False,
                  dialog_interrupted=False, reciprocal_clarification=True,
                  refinement_insufficient=False, delta_reg=1.0,
                  requires_incremental=False, reentry=False):
    """Helper function to instantiate ContextualSignals with default fallbacks."""
    return ContextualSignal(
        kappa=kappa, rho=rho, epsilon=epsilon, delta_dist=delta_dist, iota=iota,
        delta_dialog=delta_dialog, i_avail=i_avail, i_req=i_req,
        receiver_response=receiver_response, instability=instability,
        requires_articulation=requires_articulation,
        dialog_interrupted_deferred_or_structurally_constrained=dialog_interrupted,
        reciprocal_clarification_available=reciprocal_clarification,
        refinement_remains_insufficient=refinement_insufficient,
        delta_reg=delta_reg, requires_incremental_articulation=requires_incremental,
        constitutes_reentry_into_prior_modes=reentry
    )

def run_empirical_simulation():
    print("--- INITIATING ELM MULTI-AGENT FSM SIMULATION ---\n")
    
    # 1. Define the FSM Thresholds (The "Personality" / Environmental Baselines)
    # We set strict thresholds for clarity, emotion, and relational instability.
    fsm = elm_fsm(kappa_star=0.5, rho_star=0.5, epsilon_star=0.7, delta_dist_star=0.6, iota_star=0.6)
    
    # Start at the Input Layer
    current_state = fsm.q0
    print(f"Initial State: {current_state}")

    # 2. Define the Interaction Timeline (The empirical data stream)
    timeline = [
        # t=0: The Inciting Incident. 
        # High emotion (0.9), low clarity (0.2). Dialogue is available.
        create_signal(kappa=0.2, epsilon=0.9, delta_dialog=1, i_avail=0.2, i_req=0.8),
        
        # t=1: First recursive loop.
        # Agents exchange 'Provisional Whys'. Clarity improves (0.5), but still < req (0.8).
        create_signal(kappa=0.4, epsilon=0.8, delta_dialog=1, i_avail=0.5, i_req=0.8),
        
        # t=2: Breakthrough. 
        # Missing context acquired! Available info (0.9) > Required (0.8). Emotion drops (0.4).
        create_signal(kappa=0.8, epsilon=0.4, delta_dialog=1, i_avail=0.9, i_req=0.8),
        
        # t=3: The Behavioral Test.
        # Inside the Stabilization Handler. A forward step is proposed and accepted (delta_reg > 0).
        create_signal(delta_reg=1.5)
    ]

    # 3. Execute the FSM Routing
    for t, signal in enumerate(timeline):
        print(f"\n[Time Step t={t}] Incoming Signal -> Emotion: {signal.epsilon}, Info Avail: {signal.i_avail}/{signal.i_req}")
        
        # Evaluate the state-transition function (delta)
        next_state = fsm.delta(current_state, signal)
        
        # Log empirical routing data
        print(f"   Route Execution: {current_state} ---> {next_state}")
        current_state = next_state
        
        # Check for successful termination
        if current_state == "q_closure":
            print("\n*** SIMULATION TERMINATED: Contextual Sufficiency Criterion (CSC) achieved. Behavioral Closure Reached. ***")
            break

if __name__ == "__main__":
    run_empirical_simulation()
