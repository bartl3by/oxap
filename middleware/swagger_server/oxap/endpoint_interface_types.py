appsuite_soap = "appsuite-soap"
dovecot_ldap_dovecotMailboxUid = "dovecot-ldap-dovecotMailboxUid"
dovecot_ldap_dovecotMailPrimaryAddress = "dovecot-ldap-dovecotMailPrimaryAddress"
dovecot_ldap_dovecotMailAliasAddress = "dovecot-ldap-dovecotMailAliasAddress"
dovecot_ldap_dovecotUserQuotaStorage = "dovecot-ldap-dovecotUserQuotaStorage"

def AppsuiteSOAP() -> str:
    return appsuite_soap

def ldapDovecotMailboxUid() -> str:
    return dovecot_ldap_dovecotMailboxUid

def ldapDovecotMailPrimaryAddress() -> str:
    return dovecot_ldap_dovecotMailPrimaryAddress

def ldapDovecotMailAliasAddress() -> str:
    return dovecot_ldap_dovecotMailAliasAddress

def ldapDovecotUserQuotaStorage() -> str:
    return dovecot_ldap_dovecotUserQuotaStorage
