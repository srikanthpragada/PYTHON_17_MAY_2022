def show_info(**kwargs):
    print('Name  = ', kwargs.get('name', 'Unknown'))
    print('Email = ', kwargs.get('email', 'Unknown'))


show_info(name="Rossum", age=55, email="vrossum@microsoft.com")
show_info(name="James", age=55)