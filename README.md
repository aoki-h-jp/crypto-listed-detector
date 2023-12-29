# crypto-listed-detector

Docker Image for detecting cryptocurrency listings. Notify to Discord.

## docker
```bash
docker build -t crypto-listed-detector .
docker run -d -e DISCORD_WEBHOOK_URL="YOUR_URL" -it --rm crypto-listed-detector -d
```

## Supported Exchanges
### CEX
- [x] Bybit
- [x] Gate.io
- [x] MEXC

### DEX
Work in progress...

## pytest
Work in progress...

## If you want to report a bug or request a feature
Please create an issue on this repository!

## Disclaimer
This project is for educational purposes only. You should not construe any such information or other material as legal,
tax, investment, financial, or other advice. Nothing contained here constitutes a solicitation, recommendation,
endorsement, or offer by me or any third party service provider to buy or sell any securities or other financial
instruments in this or in any other jurisdiction in which such solicitation or offer would be unlawful under the
securities laws of such jurisdiction.

Under no circumstances will I be held responsible or liable in any way for any claims, damages, losses, expenses, costs,
or liabilities whatsoever, including, without limitation, any direct or indirect damages for loss of profits.