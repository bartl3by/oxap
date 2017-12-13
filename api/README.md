# Open-Xchange SOAP Interface References

## Context Interface
| HTTP Method | Path | SOAP Call Reference |
| --- | --- | --- |
| GET | /context | listAll |
| GET | /context?search=[s] | list |
| GET | /context?database=[id] | listByDatabase |
| GET | /context?filestore=[id] | listByFilestore |
| PUT | /context | disableAll, enableAll
| POST | /context | create, createModuleAccess, createModuleAccessByName
| GET | /context/[id] | getData
| GET | /context/[id]/adminid | getAdminId
| GET | /context/[id]/contextcapabilities | getContextCapabilities
| GET | /context/[id]/accesscombinationname | getAccessCombinationName
| GET | /context/[id]/quota | listQuota
| GET | /context/[id]/moduleaccess | getModuleAccess
| GET | /context/[id]/exists | exists
| PUT | /context/[id] | change, changeModuleAccessByName, enable, changeModuleAccess, downgrade, moveContextDatabase, moveContextFilestore, changeCapabilities, changeQuota, disable
| DELETE | /context/[id] | delete

## Groups Interface
| HTTP Method | Path | SOAP Call Reference |
| --- | --- | --- |
| GET | /group | listAll
| GET | /group?search=[s] | list, getMultipleData
| GET | /group/defaultgroup | getDefaultGroup
| GET | /group?user=[uid] | listGroupsForUser
| POST | groups | create
| PUT | /group | deleteMultiple
| GET | /group/[id] | getData
| PUT | groups/[id] | change
| DELETE | groups/[id] | delete
| GET | /group/[id]/member | getMembers
| POST | /group/[id]/member | addMember
| DELETE | /group/[id]/member/[id | removeMember

## Publications Interface
| HTTP Method | Path | SOAP Call Reference |
| --- | --- | --- |
| GET | /publication | getPublication
| PUT | /publication | deletePublication

## Resources Interface
| HTTP Method | Path | SOAP Call Reference |
| --- | --- | --- |
| GET | /resource | listAll
| GET | /resource/find | list, (getMultipleData)
| POST | resource | create
| GET | /resource/[id] | getData
| PUT | /resource/[id] | change
| DELETE | /resource/[id] | delete

## Users Interface
| HTTP Method | Path | SOAP Call Reference |
| --- | --- | --- |
| GET | /user | listAll
| GET | /user?search=[s] | list, getMultipleData
| POST | users | create, createByModuleAccess, createByModuleAccessName
| PUT | /user | changeModuleAccessGlobal, changeByModuleAccessName, changeByModuleAccess
| DELETE | /user | deleteMultiple
| GET | /user/[id] | getData, getUserCapabilities, getContextAdmin, getAccessCombinationName, exists, getModuleAccess
| PUT | /user/[id] | move*, changeMailAddressPersonal, changeCapabilities, change
| DELETE | /user/[id] | delete

## Util Interface
| HTTP Method | Path | SOAP Call Reference |
| --- | --- | --- |
| GET | /environment/tasks | getJobList
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

# Additional Interfaces (OXAP specific)
| HTTP Method | Path | Action |
| --- | --- | --- |
| ? | /oxap/account| ? |
| ? | /oxap/account/provisioningendpoints | ? |
| ? | /oxap/account/provisioningendpoints/appsuite | ? |
| ? | /oxap/account/provisioningendpoints/dovecot | ? |
| ? | /oxap/account/provisioningendpoints/domains | ? |
| ? | /oxap/account/provisioningendpoints/domains/[id] | ? |

# SOAP Object Overview
| Module | Object Name | Object Type |
| --- | --- | --- |
| Context | average_size | long |
| Context | enabled | boolean |
| Context | filestoreId | int |
| Context | filestore_name | string |
| Context | id | int |
| Context | loginMappings | string |
| Context | maxQuota | long |
| Context | name | string |
| Context | readDatabase | OX.Database |
| Context | usedQuota | long |
| Context | userAttributes | OX.SOAPStringMapMap |
| Context | writeDatabase | OX.Database |
| Group | displayname | string |
| Group | id | int |
| Group | members | int |
| Group | name | string |
| User | username | string |
| User | aliases | string |
| User | anniversary | date
| User | assistant_name | string |
| User | birthday | date
| User | branches | string |
| User | business_category | string |
| User | categories | string |
| User | cellular_telephone1 | string |
| User | cellular_telephone2 | string |
| User | city_business | string |
| User | city_home | string |
| User | city_other | string |
| User | commercial_register | string |
| User | company | string |
| User | contextadmin | boolean |
| User | country_business | string |
| User | country_home | string |
| User | country_other | string |
| User | defaultSenderAddress | string |
| User | driveUserFolderMode | string |
| User | default_group | OX.Group
| User | department | string |
| User | display_name | string |
| User | email1 | string |
| User | email2 | string |
| User | email3 | string |
| User | employeeType | string |
| User | fax_business | string |
| User | fax_home | string |
| User | fax_other | string |
| User | filestoreId | int |
| User | filestore_name | string |
| User | folderTree | int |
| User | given_name | string |
| User | guiPreferencesForSoap | OX.SOAPStringMap |
| User | gui_spam_filter_enabled | boolean |
| User | id | int |
| User | imapLogin | string |
| User | imapPort | int |
| User | imapSchema | string |
| User | imapServer | string |
| User | imapServerString | string |
| User | info | string |
| User | instant_messenger1 | string |
| User | instant_messenger2 | string |
| User | language | string |
| User | mail_folder_confirmed_ham_name | string |
| User | mail_folder_confirmed_spam_name | string |
| User | mail_folder_drafts_name | string |
| User | mail_folder_sent_name | string |
| User | mail_folder_spam_name | string |
| User | mail_folder_trash_name | string |
| User | mailenabled | boolean |
| User | manager_name | string |
| User | marital_status | string |
| User | maxQuota | long |
| User | middle_name | string |
| User | name | string |
| User | nickname | string |
| User | note | string |
| User | number_of_children | string |
| User | number_of_employee | string |
| User | password | string |
| User | passwordMech | string |
| User | password_expired | boolean |
| User | position | string |
| User | postal_code_business | string |
| User | postal_code_home | string |
| User | postal_code_other | string |
| User | primaryEmail | string |
| User | profession | string |
| User | room_number | string |
| User | sales_volume | string |
| User | smtpPort | int |
| User | smtpSchema | string |
| User | smtpServer | string |
| User | smtpServerString | string |
| User | spouse_name | string |
| User | state_business | string |
| User | state_home | string |
| User | state_other | string |
| User | street_business | string |
| User | street_home | string |
| User | street_other | string |
| User | suffix | string |
| User | sur_name | string |
| User | tax_id | string |
| User | telephone_assistant | string |
| User | telephone_business1 | string |
| User | telephone_business2 | string |
| User | telephone_callback | string |
| User | telephone_car | string |
| User | telephone_company | string |
| User | telephone_home1 | string |
| User | telephone_home2 | string |
| User | telephone_ip | string |
| User | telephone_isdn | string |
| User | telephone_other | string |
| User | telephone_pager | string |
| User | telephone_primary | string |
| User | telephone_radio | string |
| User | telephone_telex | string |
| User | telephone_ttytdd | string |
| User | timezone | string |
| User | title | string |
| User | uploadFileSizeLimit | int |
| User | uploadFileSizeLimitPerFile | int |
| User | url | string |
| User | usedQuota | long |
| User | userAttributes | OX.SOAPStringMapMap |
| User | userfield01 | string |
| User | userfield02 | string |
| User | userfield03 | string |
| User | userfield04 | string |
| User | userfield05 | string |
| User | userfield06 | string |
| User | userfield07 | string |
| User | userfield08 | string |
| User | userfield09 | string |
| User | userfield10 | string |
| User | userfield11 | string |
| User | userfield12 | string |
| User | userfield13 | string |
| User | userfield14 | string |
| User | userfield15 | string |
| User | userfield16 | string |
| User | userfield17 | string |
| User | userfield18 | string |
| User | userfield19 | string |
| User | userfield20 | string |
| User | primaryAccountName | string |
| User | convert_drive_user_folders | boolean |
| User Module Access | OLOX20 | boolean |
| User Module Access | USM | boolean |
| User Module Access | activeSync | boolean |
| User Module Access | calendar | boolean |
| User Module Access | collectEmailAddresses | boolean |
| User Module Access | contacts | boolean |
| User Module Access | delegateTask | boolean |
| User Module Access | deniedPortal | boolean |
| User Module Access | editGroup | boolean |
| User Module Access | editPassword | boolean |
| User Module Access | editPublicFolders | boolean |
| User Module Access | editResource | boolean |
| User Module Access | globalAddressBookDisabled | boolean |
| User Module Access | ical | boolean |
| User Module Access | infostore | boolean |
| User Module Access | multipleMailAccounts | boolean |
| User Module Access | publicFolderEditable | boolean |
| User Module Access | publication | boolean |
| User Module Access | readCreateSharedFolders | boolean |
| User Module Access | subscription | boolean |
| User Module Access | syncml | boolean |
| User Module Access | tasks | boolean |
| User Module Access | vcard | boolean |
| User Module Access | webdav | boolean |
| User Module Access | webdavXml | boolean |
| User Module Access | webmail | boolean |
| Database | clusterWeight | int |
| Database | currentUnits | int |
| Database | driver | string |
| Database | id | int |
| Database | login | string |
| Database | master | boolean |
| Database | masterId | int |
| Database | maxUnits | int |
| Database | name | string |
| Database | password | string |
| Database | poolHardLimit | int |
| Database | poolInitial | int |
| Database | poolMax | int |
| Database | read_id | int |
| Database | scheme | string |
| Database | url | string |
| Filestore | currentContexts | int |
| Filestore | id | int |
| Filestore | maxContexts | int |
| Filestore | reserved | long |
| Filestore | size | long |
| Filestore | url | string |
| Filestore | used | long |
| Publication | userId | int |
| Publication | context  | OX.Context
| Publication | id | string |
| Publication | entityId | string |
| Publication | module | string |
| Publication | name | string |
| Publication | description | string |
| Credentials | login | string |
| Credentials | password | string |
| String Map Map | entries | OX.SOAPMapEntry |
| String Map Entry | key | string |
| String Map Entry | value | OX.SOAPStringMap |
| String Map | entries | OX.Entry |
| Entry | key | string |
| Entry | value | string |