connect('username','userpass','t3://localhost:7001')
domainRuntime()
cd('AppRuntimeStateRuntime/AppRuntimeStateRuntime')
#cd('ServerRuntimes')
#ls()
AppList = cmo.getApplicationIds()
print '####### Application #######  Application State\n'
print '***********************************************\n'
for App in AppList:
    print '#######',App ,' #######', cmo.getIntendedState(App)

print '***********************************************\n'
