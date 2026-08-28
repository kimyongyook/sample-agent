# sample-agent

`code-review-agent` POC를 검증하기 위한 작은 Python 샘플 프로젝트입니다.

애플리케이션 자체에는 LLM 또는 Simflow 연동 코드가 없습니다. 일반 Python 코드와
테스트만 두고, pull request에서 별도의 코드 리뷰 Action이 변경사항을 분석합니다.

## 테스트

```bash
python -m unittest discover -s tests -v
```

## AI 코드 리뷰 설정

저장소의 **Settings → Secrets and variables → Actions → Repository secrets**에서
`SIMFLOW_API_KEY`를 추가해야 합니다. 실제 키는 소스나 workflow 파일에 넣지 않습니다.
