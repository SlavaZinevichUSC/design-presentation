from system.system import ui

#Lets use our application!
validate_vm = ui.get_validate_vm('user')
validate_vm.display()
validate_vm.validate('user')

login_vm = ui.get_login_vm()
login_vm.display()
interactive_vm = login_vm.login('user', '0000')
interactive_vm.display()
interactive_vm.update_balance(100)
interactive_vm.show_balance()
ui.save(interactive_vm)