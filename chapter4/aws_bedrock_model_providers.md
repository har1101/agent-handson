# AWS Bedrockで利用可能なモデルプロバイダー

AWS Bedrockは複数のモデルプロバイダーから高性能なファンデーションモデル(FM)を提供しています。以下はBedrockで利用できる主要なモデルプロバイダーとそのモデルの一覧です。

## モデルプロバイダー一覧

AWS Bedrockでは、以下のモデルプロバイダーのAIモデルが利用可能です：

1. **Amazon (Titan)** - AWSが独自に開発したファンデーションモデル
2. **Anthropic (Claude)** - 高性能な対話型AI
3. **AI21 Labs** - Jamba、Jurassic-2シリーズ
4. **Cohere** - Command、Command Light、Command R、Command R+
5. **Meta** - Llama 2、Llama 3、Llama 3.1、Llama 3.2、Llama 4シリーズ
6. **Mistral AI** - Mistral Instruct、Mistral Large、Mistral Small
7. **DeepSeek** - DeepSeek-R1
8. **Pixtral** - Pixtral Large
9. **Writer** - Palmyra X4、Palmyra X5

## 主要モデルの機能対応

各モデルは以下のような機能をサポートしています：

| モデルプロバイダー | チャット機能 | ストリーミング | システムプロンプト | ドキュメントチャット | 画像認識 | ツール使用 | ガードレール |
|------------|-------|-----------|------------|--------------|-------|--------|----------|
| Amazon Titan | ○ | ○ | × | ほとんど○ | × | × | ○ |
| Anthropic Claude 3 | ○ | ○ | ○ | ○ | ○ | ○ | ○ |
| Anthropic Claude 3.5/3.7 | ○ | ○ | ○ | ○ | ○ | ○ | ○/× |
| Anthropic Claude 4 | ○ | ○ | ○ | ○ | ○ | ○ | × |
| AI21 Jamba | ○ | ○ | ○ | ○ | × | ○ | ○ |
| AI21 Jurassic-2 | 制限あり | × | × | × | × | × | ○ |
| Cohere Command | 制限あり | 制限あり | × | ○ | × | × | ○ |
| Cohere Command R/R+ | ○ | ○ | ○ | ○ | × | ○ | × |
| Meta Llama 3 | ○ | ○ | ○ | ○ | × | × | ○ |
| Meta Llama 3.1/3.2 | ○ | ○ | ○ | ○ | 一部○ | 一部○ | ○ |
| Meta Llama 4 | ○ | ○ | ○ | ○ | ○ | ○ | ○ |
| Mistral AI | ○ | ○ | 一部○ | ○ | × | 一部○ | ○ |
| DeepSeek-R1 | ○ | ○ | ○ | ○ | × | × | ○ |
| Pixtral Large | ○ | ○ | ○ | ○ | × | ○ | ○ |
| Writer Palmyra | ○ | ○ | ○ | ○ | × | ○ | ○ |

## Amazon Titanモデル

AWSが独自開発した以下のモデルが利用可能です：

* **Amazon Titan Text** - テキスト生成モデル
* **Amazon Titan Text Embeddings V2** - テキスト埋め込みモデル
* **Amazon Titan Multimodal Embeddings G1** - マルチモーダル埋め込みモデル
* **Amazon Titan Image Generator G1 V1** - 画像生成モデル
* **Amazon Nova シリーズ** (Premier, Pro, Lite, Micro) - 最新の高性能モデルファミリー

## 注意点

* CoherenとAI21の一部モデルはチャット機能に制限があり、会話の履歴を維持できません
* 画像認識（Vision）機能は一部のモデルでのみサポートされています
* ツール使用（Tool use）機能も限定的なモデルでのみ利用可能です
* リージョンによってサポートされているモデルが異なる場合があります

AWS Bedrockは継続的に新しいモデルを追加しており、利用可能なモデルとその機能は今後も拡張される予定です。