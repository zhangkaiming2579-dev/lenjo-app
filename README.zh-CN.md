# 练境 Lenjo — AI 健身教练与训练记录

**练境是一款本地优先的 AI 健身教练与健身管理 App，适用于 iPhone，可选配 Apple Watch。** 支持拍照识别热量、卡路里估算、饮食管理与三大营养素记录。把训练计划、每组实际完成情况、恢复状态和饮食放在一起，帮助你判断下一次怎么练。

**官网：[lenjoapp.com](https://lenjoapp.com/)** · [App Store 下载](https://apps.apple.com/app/id6784486285) · [中文产品页](https://zhangkaiming2579-dev.github.io/lenjo-app/zh/) · [English](README.md) · [联系作者](https://lenjoapp.com/support.html)

## 产品信息

| 项目 | 信息 |
| --- | --- |
| 产品名称 | 练境 / Lenjo |
| 类型 | AI 健身教练、力量训练记录、饮食记录 |
| App Store ID | 6784486285 |
| 支持设备 | iOS 17 及以上的 iPhone；可选 watchOS 10 及以上的 Apple Watch |
| 产品支持 | 练境 / Lenjo |
| 免费与付费 | iPhone 训练执行与记录免费；Lenjo Pro 为可选订阅 |
| 官网 | https://lenjoapp.com/ |
| 联系邮箱 | KmTech2026@outlook.com |

## 核心流程

1. 告诉教练目标、经验、器械和可用时间，请求训练计划。
2. 审核并修改动作、组数、次数、重量和休息，再开始训练。
3. 逐组记录实际重量、次数、RPE 和完成状态，训练结束后保存。
4. 用已保存的记录和恢复感受讨论下一次加重、维持、减量或调整。

你也可以直接开始自由训练。有氧训练支持按分钟记录，并按项目填写速度、坡度或距离。Pro 用户可把计划发到 Apple Watch，在手腕上记录训练；在权限和数据可用时查看实时心率、组间恢复参考及训练后的逐组心率时间轴。

饮食支持手动记录或拍照分析。AI 估算食物、热量、蛋白质、碳水与脂肪，你检查并调整结果后再确认保存。体重、活动、恢复和训练趋势可回看；长期记忆可以查看、编辑和删除。

AI 饮食讨论可以结合已保存的饮食、体重目标和训练安排，询问蛋白摄入或训练前后吃什么。建议需要审核，记录不完整时应先补充信息。

## 按使用问题查功能

[中文功能指南](https://zhangkaiming2579-dev.github.io/lenjo-app/zh/guide/)覆盖 14 个场景，每个叫法都有解释，并给出实际操作问题。也可直接阅读[本仓库 Markdown 版](docs/feature-guide.zh-CN.md)或[英文版](docs/feature-guide.md)。

| 想解决的问题 | 功能入口与说明 |
| --- | --- |
| 这顿饭有多少卡路里？ | [拍照识别热量、食物识别与大卡估算](docs/feature-guide.zh-CN.md#photo-calories)，检查份量和配料后确认。 |
| 怎么记录每天吃了什么？ | [饮食管理、饮食日记与热量记录](docs/feature-guide.zh-CN.md#food-log)，支持手动输入。 |
| 蛋白质、碳水和脂肪能记录吗？ | [三大营养素与蛋白摄入记录](docs/feature-guide.zh-CN.md#food-log)，照片结果为待确认估算。 |
| AI 饮食怎么结合减脂或增肌目标？ | [营养分析与训练前后饮食讨论](docs/feature-guide.zh-CN.md#ai-nutrition)，基于保存的记录提供参考。 |
| AI 健身教练能安排今天练什么吗？ | [AI 教练与训练计划](docs/feature-guide.zh-CN.md#plans)，说明目标、器械和时长。 |
| 健身管理能保存每组实际重量吗？ | [训练日志、逐组记录、补记与文本导入](docs/feature-guide.zh-CN.md#workout-log)，保存后用于复盘。 |
| 什么时候该加重量或次数？ | [力量训练、渐进超负荷与训练量](docs/feature-guide.zh-CN.md#strength-progress)，结合 RPE 和恢复讨论。 |
| 新手、居家或只有哑铃怎么练？ | [有限器械与有限时间的训练安排](docs/feature-guide.zh-CN.md#beginner-home)，审核建议是否适合自己。 |
| 苹果手表能记录训练与组间恢复吗？ | [Apple Watch 腕上训练](docs/feature-guide.zh-CN.md#watch)，需要 Pro、配对与相关授权。 |
| 有氧、体重和训练进度怎么回看？ | [有氧计时](docs/feature-guide.zh-CN.md#cardio)与[体重、训练日历和趋势](docs/feature-guide.zh-CN.md#body-progress)。 |
| 不认识器械或想记录体测报告？ | [器械与身体成分报告识别](docs/feature-guide.zh-CN.md#recognition)，检查结果后再确认。 |
| 不想使用 AI，或想纠正教练记忆？ | [本地记录、健康授权与可编辑记忆](docs/feature-guide.zh-CN.md#local-memory)。 |

## 官网上的更多内容

这里是产品资料摘要。完整的训练指南、对比和免费计算器在官网：

- [Fitbod 替代：练到一半也能问的 AI 健身教练](https://lenjoapp.com/fitbod-alternative/)
- [免费健身计算器](https://lenjoapp.com/tools/)：[1RM](https://lenjoapp.com/tools/one-rep-max/)、[杠铃配重](https://lenjoapp.com/tools/plates/)、[每日热量 TDEE](https://lenjoapp.com/tools/tdee/)、[蛋白质](https://lenjoapp.com/tools/protein/)、[食物热量](https://lenjoapp.com/tools/food-calories/)
- [AI 力量训练计划怎么制定](https://lenjoapp.com/guides/ai-strength-training-plan/) · [RPE 训练计划指南](https://lenjoapp.com/guides/rpe-training-plan/) · [今天该训练还是休息](https://lenjoapp.com/guides/train-or-rest-today/)

## 免费与 Pro

iPhone 训练执行与记录免费，并提供 AI 体验额度。Lenjo Pro 提供 Apple Watch 训练执行与恢复参考、更高 AI 教练和照片分析额度、深度报告。月付与年付提供相同的 Pro 权益，当前价格、试用资格和额度以 App 内与 App Store 为准。

## 数据与边界

核心记录主要保存在本机，Apple 登录和 Apple 健康授权均为可选。AI 教练和照片分析需要联网，相关内容在说明与同意后经练境网关发送给第三方模型服务商。拒绝 AI 处理后，仍可使用本地训练和记录。

练境提供健身、训练、恢复和饮食参考，不提供医疗诊断或治疗。照片营养估算需要确认，恢复就绪提示用于训练节奏参考。

[隐私政策](https://lenjoapp.com/privacy.html) · [使用条款](https://lenjoapp.com/terms.html) · [常见问题](docs/faq.md) · [上手步骤](docs/getting-started.md)

## 联系与反馈

联系方式：[KmTech2026@outlook.com](mailto:KmTech2026@outlook.com)，或使用[官网支持页](https://lenjoapp.com/support.html)。公开反馈请勿包含个人健康资料、聊天原文或未经处理的诊断附件。

本仓库用于公开产品介绍和反馈，App 源码不在此发布。产品信息核对日期：2026-10-11；已发布功能与供应情况以 App Store 为准。
