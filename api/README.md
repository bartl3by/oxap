# Open-Xchange SOAP References

## Context Interface
| HTTP Method | Path | SOAP Call Reference |
| --- | --- | --- |
| GET | /contexts | listAll |
| GET | /contexts?search=[s] | list |
| GET | /contexts?database=[id] | listByDatabase |
| GET | /contexts?filestore=[id] | listByFilestore |
| PUT | /contexts | disableAll, enableAll
| POST | /contexts | create, createModuleAccess, createModuleAccessByName
| GET | /contexts/[id] | getData
| GET | /contexts/[id]/adminid | getAdminId
| GET | /contexts/[id]/contextcapabilities | getContextCapabilities
| GET | /contexts/[id]/accesscombinationname | getAccessCombinationName
| GET | /contexts/[id]/quota | listQuota
| GET | /contexts/[id]/moduleaccess | getModuleAccess
| GET | /contexts/[id]/exists | exists
| PUT | /contexts/[id] | change, changeModuleAccessByName, enable, changeModuleAccess, downgrade, moveContextDatabase, moveContextFilestore, changeCapabilities, changeQuota, disable
| DELETE | /contexts/[id] | delete

## Groups Interface
| HTTP Method | Path | SOAP Call Reference |
| --- | --- | --- |
| GET | /groups | listAll
| GET | /groups?search=[s] | list, getMultipleData
| GET | /groups/defaultgroup | getDefaultGroup
| GET | /groups?user=[uid] | listGroupsForUser
| POST | groups | create
| PUT | /groups | deleteMultiple
| GET | /groups/[id] | getData
| PUT | groups/[id] | change
| DELETE | groups/[id] | delete
| GET | /groups/[id]/member | getMembers
| POST | /groups/[id]/member | addMember
| DELETE | /groups/[id]/member/[id | removeMember

## Publications Interface
| HTTP Method | Path | SOAP Call Reference |
| --- | --- | --- |
| GET | publications | getPublication
| PUT | /publications | deletePublication

## Resources Interface
| HTTP Method | Path | SOAP Call Reference |
| --- | --- | --- |
| GET | /resources | listAll
| GET | /resources/find | list, (getMultipleData)
| POST | resources | create
| GET | /resources/[id] | getData
| PUT | /resources/[id] | change
| DELETE | /resources/[id] | delete

## Users Interface
| HTTP Method | Path | SOAP Call Reference |
| --- | --- | --- |
| GET | /users | listAll
| GET | /users?search=[s] | list, getMultipleData
| POST | users | create, createByModuleAccess, createByModuleAccessName
| PUT | /users | changeModuleAccessGlobal, changeByModuleAccessName, changeByModuleAccess
| DELETE | /users | deleteMultiple
| GET | /users/[id] | getData, getUserCapabilities, getContextAdmin, getAccessCombinationName, exists, getModuleAccess
| PUT | /users/[id] | move*, changeMailAddressPersonal, changeCapabilities, change
| DELETE | /users/[id] | delete

## Util Interface
| HTTP Method | Path | SOAP Call Reference |
| --- | --- | --- |
| GET | environment/tasks | getJobList
| PUT | /environment/tasks | flush
| GET | /environment/tasks/[id] | getTaskResults
| DELETE | /environment/tasks/[id] | deleteJob
| GET | /environment/databases | listAllDatabase
| POST | /environment/databases | registerDatabase
| GET | /environment/databases/[id] | listDatabase
| PUT | /environment/databases/[id] | changeDatabase, unblockDatabase, checkDatabase
| DELETE | /environment/databases/[id] | unregisterDatabase
| GET | /environment/filestores | listAllFilestore
| POST | /environment/filestores | registerFilestore
| GET | /environment/filestores/[id] | listFilestore
| PUT | /environment/filestores/[id] | changeFilestore
| DELETE | /environment/filestores/[id] | unregisterFilestore
| GET | /environment/servers | listAllServer
| POST | environment/servers | registerServer
| GET | /environment/servers/[id] | listServer
| DELETE | /environment/servers/[id] | unregisterServer
| GET | environment/maintenance | listAllMaintenanceReason
| POST | /environment/maintenance | createMaintenanceReason
| GET | /environment/maintenance/[id] | listMaintenanceReason
| DELETE | /environment/maintenance/[id] | deleteMaintenanceReason

# OXAP Specific
| HTTP Method | Path | Action |
| --- | --- | --- |
| ? | /account| ? |
| ? | /account/provisioningendpoints | ? |
| ? | /account/provisioningendpoints/appsuite | ? |
| ? | /account/provisioningendpoints/dovecot | ? |
| ? | /account/provisioningendpoints/domains | ? |
| ? | /account/provisioningendpoints/domains/[id] | ? |