
# when we add an asterix to a parameter, Python will see that as a dictionary
def save_user(**user):
    print(user)


# here we should pass keword arguments
save_user(id=1, name="admin", age=36)
