TEAMS = "teams"
RBAC = "rbac"
SSO = "sso"
SUPPORT = "support"
AUDIT_LOG = "audit_log"
METRICS = "metrics"
SECURE_FILE_SERVE = "secure_file_serve"
ENTERPRISE_SETTINGS = "ENTERPRISE_SETTINGS"
DATA_SYNC = "data_sync"
CHART_WIDGET = "chart_widget"
ADVANCED_WEBHOOKS = "advanced_webhooks"

BUILDER_SSO = "application_user_sso"
def has_feature(feature, license=None, user=None):
    # You can log features being accessed if you want
    print(f"[MAS Patch] Feature accessed: {feature}")
    return True
