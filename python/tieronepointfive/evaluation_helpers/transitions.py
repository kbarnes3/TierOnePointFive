from collections import namedtuple

TransitionRule = namedtuple('TransitionRule', ['start_state', 'next_state', 'is_terminal', 'requirement'])


def get_best_transition(rules, config, start_state):
    for i, rule in enumerate(rules):
        if start_state == rule.start_state:
            candidate_index = i
            break

    prioritized_rules = rules[candidate_index:] + rules[:candidate_index]
    for candidate_rule in prioritized_rules:
        if candidate_rule.requirement(config):
            return candidate_rule.next_state, candidate_rule.is_terminal
