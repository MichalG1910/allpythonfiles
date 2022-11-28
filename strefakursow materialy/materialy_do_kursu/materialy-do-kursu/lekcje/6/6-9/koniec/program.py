options = {
    'env': 'production',
    'db': 'mysql',
    'version': 1.0,
    'show_errors': True
}

options.update({
   'user': 'admin',
   'app': 0,
   'version': 2.2 
})

print(options.keys())