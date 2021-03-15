import os
 
# for k, v in os.environ.items():
#     print(f'{k}={v}')


 
# home_dir =os.environ['HOME']
# username = os.environ['USER']
# print(f'{username} home directory is {home_dir}')



#How to Check if an Environment Variable Exists?
# env_var = 'NADAV'
 
# if env_var in os.environ:
#     print(f'{env_var} value is  -> {os.environ[env_var]}')
# else:
#     print(f'{env_var} does not exist')




# env_var = input('Please enter environment variable name:\n')
 
# env_var_value = input('Please enter environment variable value:\n')
 
# os.environ[env_var] = env_var_value
 
# print(f'{env_var}={os.environ[env_var]} environment variable has been set.')




 
env_var = 'NADAV'
 
env_var_value = 'IS A DEVOPS ENGNEER'
 
os.environ[env_var] = env_var_value

print(f'{env_var}={os.environ[env_var]} environment variable has been set.')
