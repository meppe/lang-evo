
# A list of vars with their initial values.
vars = {"c": 0, "e": 0, "p": 0}


# A list of causal laws that can affect a variable.
causal_laws = {"c": [], "e": [], "p": []}

# a causal law is a triple (var, value, condition, action). The variable is the key of the dictionary entry.
# The value is a float, the condition is a list of variable-value-pairs, and the action is a string.
causal_laws["e"].append((10, [("p", 5)], "set_e"))


