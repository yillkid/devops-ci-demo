# devops-ci-demo

DevOps 入門課 **ch3〈Unit Test〉+ ch4〈GitHub Actions CI〉** 的極簡範例 repo。
一個小 FastAPI app + 測試 + 一條「只跑 pytest」的 CI——clone 下來就能直接練，push 後 CI 會自動跑測試。

> 這個 repo 刻意保持單純（沒有 Docker / K8S / 部署）。完整的 build → push → 部署 pipeline 在另一個 repo [`devops-demo`](https://github.com/4-learn/devops-demo)，那是 ch5/ch6 用的。

## 跑法

    pip install -r requirements.txt
    pytest                       # 跑全部測試
    cd examples/pytest-basics && pytest   # ch3 範例 1：測純函式

## 內容

| 路徑 | 用途 |
|------|------|
| `app/main.py` | FastAPI app：`/`、`/health` |
| `app/login.py` | `/login`（email 非空檢查）—— ch3 workshop 補測試的對象 |
| `tests/test_main.py` | endpoint 測試（ch3 範例 2 + workshop） |
| `examples/pytest-basics/` | ch3 範例 1：純函式 `check_machine` + `test_check.py` |
| `.github/workflows/ci.yml` | ch3/ch4：push / PR 自動跑 pytest |

## Test
1, 2
