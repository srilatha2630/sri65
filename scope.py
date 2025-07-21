def outer_function():
    outer_var = "I'm outside!"
    def inner_function():
        inner_var = "I'm inside!"
        print(inner_var)  # Can access inner_var
        print(outer_var)  # Can access outer_var (because it's in the outer scope)
    inner_function()
    print(outer_var)  # Can access outer_var, but can't access inner_var outside
outer_function()
