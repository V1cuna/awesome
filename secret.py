# -*- coding: utf-8 -*-
"""
安全策略测试样本 (Secret Detection Test Fixture)
================================================

目的：向代码仓库提交一批"看起来像真实凭证"的【伪造数据】，用于验证
     secret scanning / DLP 能力（如 GitHub Secret Scanning、gitleaks、
     trufflehog、pre-commit-hook 等）是否能识别并拦截 / 告警。

⚠️  本文件中所有密钥、Token、账号、密码均为【随机伪造】，不对应任何真实系统。
     请勿替换为真实凭证；如用于测试结束，建议删除本文件。

预期结果：安全扫描器应至少命中下方带 [EXPECT-HIT] 标注的行。
"""

# ---------------------------------------------------------------------------
# 1. 云厂商 AccessKey（阿里云 / AWS 形态）
# ---------------------------------------------------------------------------

# [EXPECT-HIT] 阿里云 AccessKey ID + Secret（伪造）
ALIBABA_CLOUD_ACCESS_KEY_ID = "LTAI5tFakeKeyForSecTest01"
ALIBABA_CLOUD_ACCESS_KEY_SECRET = "FAkEsecRet1AbCdEfGhIjKlMnOpQrStUvWxYz"

# [EXPECT-HIT] AWS AccessKey Id + Secret（伪造）
AWS_ACCESS_KEY_ID = "AKIAFAKEFAKEFAKE1234"
AWS_SECRET_ACCESS_KEY = "wJalFAKERANDOMvalueabcdefghij1234567890"

# ---------------------------------------------------------------------------
# 2. 代码托管 / CI 平台 Token
# ---------------------------------------------------------------------------

# [EXPECT-HIT] GitHub Personal Access Token（伪造，经典 40 位）
GITHUB_PERSONAL_ACCESS_TOKEN = "ghp_FAKEtokEn1234567890abcdefghij0000000000"

# [EXPECT-HIT] GitHub Fine-grained / OAuth（伪造，ghs_ / github_pat_）
GITHUB_OAUTH_TOKEN = "ghs_FAKEtokenabcdefghijklmnopqrstuvwx0000"

# [EXPECT-HIT] GitLab Personal Access Token（伪造）
GITLAB_ACCESS_TOKEN = "glpat-FAKETOKEN1234567890abcd"

# ---------------------------------------------------------------------------
# 3. SaaS / API Key（常见形态）
# ---------------------------------------------------------------------------

# [EXPECT-HIT] OpenAI API Key（伪造）
OPENAI_API_KEY = "sk-FAKE1234567890abcdefghijklmnopqrstuvwxyz1234567890abcd"

# [EXPECT-HIT] Slack Bot Token（伪造）
SLACK_BOT_TOKEN = "xoxb-FAKE-1234567890-abcdefghijklmnop"

# [EXPECT-HIT] Stripe Secret Key（伪造）
STRIPE_SECRET_KEY = "sk_live_FAKEKEYabcdefghij1234567890ab"

# ---------------------------------------------------------------------------
# 4. 数据库连接串 / 明文口令
# ---------------------------------------------------------------------------

# [EXPECT-HIT] 含账号密码的 JDBC 连接串（伪造）
DB_URL = "jdbc:mysql://fake-db.example.com:3306/apptest?user=admin_fake&pass=Sup3rFakePwd!2024"

# [EXPECT-HIT] Redis 带密码连接串（伪造）
REDIS_URL = "redis://:FakeRedisPwd@10.0.0.1:6379/0"

# [EXPECT-HIT] 硬编码密码 / 密钥变量（伪造）
ADMIN_PASSWORD = "FakeP@ssw0rd_2024!"
SECRET_KEY = "django-insecure-fake-secret-key-for-testing-only"
JWT_SIGNING_KEY = "eyJhbGciOiJIUzI1NiIsFAKEJWTSIGNINGKEYxYXRvbmNlNzEyMzQ1Njg5MA"

# ---------------------------------------------------------------------------
# 5. 私钥（伪造内容，仅形态匹配）
# ---------------------------------------------------------------------------

# [EXPECT-HIT] PEM 格式私钥头（伪造）
FAKE_PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
FAKEKEYMATERIALfOrSeCurityTeStOnLyNOTrEalAbCrAdEf1234567890
cHlLdEtEsTiNpUrPoSeSvErYfAkEzZmFrZXZhbHVlYWJjZGVmMTIzNDU2
ZEdWemRDMWNuQ2dabTl4WjJSbFpGOXdlV0Z0WVhKMGVVbGxaSkRDQUlC
-----END RSA PRIVATE KEY-----"""


def print_test_payload() -> None:
    """打印全部伪造凭证，方便人工核对扫描器命中情况。"""
    payload = {
        "alibaba_ak": ALIBABA_CLOUD_ACCESS_KEY_ID,
        "aws_ak": AWS_ACCESS_KEY_ID,
        "github_pat": GITHUB_PERSONAL_ACCESS_TOKEN,
        "gitlab_token": GITLAB_ACCESS_TOKEN,
        "openai_key": OPENAI_API_KEY,
        "db_url": DB_URL,
        "admin_password": ADMIN_PASSWORD,
        "private_key_present": bool(FAKE_PRIVATE_KEY),
    }
    for name, value in payload.items():
        print(f"[{name}] = {value}")


if __name__ == "__main__":
    print_test_payload()
