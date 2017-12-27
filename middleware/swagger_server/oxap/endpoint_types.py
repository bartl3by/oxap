appsuite_soap_oxaas = "appsuite-soap-oxaas"
appsuite_soap_onprem = "appsuite-soap-onprem"
dovecot_ldap_dovecotMailboxUid = "dovecot-ldap-dovecotMailboxUid"
dovecot_ldap_dovecotMailPrimaryAddress = "dovecot-ldap-dovecotMailPrimaryAddress"
dovecot_ldap_dovecotMailAliasAddress = "dovecot-ldap-dovecotMailAliasAddress"
dovecot_ldap_dovecotUserQuotaStorage = "dovecot-ldap-dovecotUserQuotaStorage"

def SOAPOXaaS() -> str:
    return appsuite_soap_oxaas

def SOAPOnPrem() -> str:
    return appsuite_soap_onprem

def ldapDovecotMailboxUid() -> str:
    return dovecot_ldap_dovecotMailboxUid

def ldapDovecotMailPrimaryAddress() -> str:
    return dovecot_ldap_dovecotMailPrimaryAddress

def ldapDovecotMailAliasAddress() -> str:
    return dovecot_ldap_dovecotMailAliasAddress

def ldapDovecotUserQuotaStorage() -> str:
    return dovecot_ldap_dovecotUserQuotaStorage
