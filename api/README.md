# Open-Xchange SOAP Interface References

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

# Additional Interfaces (OXAP specific)
| HTTP Method | Path | Action |
| --- | --- | --- |
| ? | /account| ? |
| ? | /account/provisioningendpoints | ? |
| ? | /account/provisioningendpoints/appsuite | ? |
| ? | /account/provisioningendpoints/dovecot | ? |
| ? | /account/provisioningendpoints/domains | ? |
| ? | /account/provisioningendpoints/domains/[id] | ? |

# SOAP Object Overview

## Context ##

average_size: long
enabled: boolean
filestoreId: int
filestore_name: string
id: int
loginMappings: string
maxQuota: long
name: string
readDatabase: OX.Database
usedQuota: long
userAttributes: OX.SOAPStringMapMap
writeDatabase: OX.Database

## Group ##

displayname: string
id: int
members: int
name: string

## User ##

aliases: string
anniversary: date
assistant_name: string
birthday: date
branches: string
business_category: string
categories: string
cellular_telephone1: string
cellular_telephone2: string
city_business: string
city_home: string
city_other: string
commercial_register: string
company: string
contextadmin: boolean
country_business: string
country_home: string
country_other: string
defaultSenderAddress: string
driveUserFolderMode: string
default_group: OX.Group
department: string
display_name: string
email1: string
email2: string
email3: string
employeeType: string
fax_business: string
fax_home: string
fax_other: string
filestoreId: int
filestore_name: string
folderTree: int
given_name: string
guiPreferencesForSoap: OX.SOAPStringMap
gui_spam_filter_enabled: boolean
id: int
imapLogin: string
imapPort: int
imapSchema: string
imapServer: string
imapServerString: string
info: string
instant_messenger1: string
instant_messenger2: string
language: string
mail_folder_confirmed_ham_name: string
mail_folder_confirmed_spam_name: string
mail_folder_drafts_name: string
mail_folder_sent_name: string
mail_folder_spam_name: string
mail_folder_trash_name: string
mailenabled: boolean
manager_name: string
marital_status: string
maxQuota: long
middle_name: string
name: string
nickname: string
note: string
number_of_children: string
number_of_employee: string
password: string
passwordMech: string
password_expired: boolean
position: string
postal_code_business: string
postal_code_home: string
postal_code_other: string
primaryEmail: string
profession: string
room_number: string
sales_volume: string
smtpPort: int
smtpSchema: string
smtpServer: string
smtpServerString: string
spouse_name: string
state_business: string
state_home: string
state_other: string
street_business: string
street_home: string
street_other: string
suffix: string
sur_name: string
tax_id: string
telephone_assistant: string
telephone_business1: string
telephone_business2: string
telephone_callback: string
telephone_car: string
telephone_company: string
telephone_home1: string
telephone_home2: string
telephone_ip: string
telephone_isdn: string
telephone_other: string
telephone_pager: string
telephone_primary: string
telephone_radio: string
telephone_telex: string
telephone_ttytdd: string
timezone: string
title: string
uploadFileSizeLimit: int
uploadFileSizeLimitPerFile: int
url: string
usedQuota: long
userAttributes: OX.SOAPStringMapMap
userfield01: string
userfield02: string
userfield03: string
userfield04: string
userfield05: string
userfield06: string
userfield07: string
userfield08: string
userfield09: string
userfield10: string
userfield11: string
userfield12: string
userfield13: string
userfield14: string
userfield15: string
userfield16: string
userfield17: string
userfield18: string
userfield19: string
userfield20: string
primaryAccountName: string
convert_drive_user_folders: boolean

## User Module Access ##

OLOX20: boolean
USM: boolean
activeSync: boolean
calendar: boolean
collectEmailAddresses: boolean
contacts: boolean
delegateTask: boolean
deniedPortal: boolean
editGroup: boolean
editPassword: boolean
editPublicFolders: boolean
editResource: boolean
globalAddressBookDisabled: boolean
ical: boolean
infostore: boolean
multipleMailAccounts: boolean
publicFolderEditable: boolean
publication: boolean
readCreateSharedFolders: boolean
subscription: boolean
syncml: boolean
tasks: boolean
vcard: boolean
webdav: boolean
webdavXml: boolean
webmail: boolean


## Database ##

clusterWeight: int
currentUnits: int
driver: string
id: int
login: string
master: boolean
masterId: int
maxUnits: int
name: string
password: string
poolHardLimit: int
poolInitial: int
poolMax: int
read_id: int
scheme: string
url: string

## Filestore ##

currentContexts: int
id: int
maxContexts: int
reserved: long
size: long
url: string
used: long

## Publication

userId: int
context: : OX.Context
id: string
entityId: string
module: string
name: string
description: string

## Credentials ##

login: string
password: string

## String Map Map ##

entries: OX.SOAPMapEntry

## Map Entry ##

key: string
value: OX.SOAPStringMap

## String Map ##

entries: OX.Entry

## Entry ##

key: string
value: string