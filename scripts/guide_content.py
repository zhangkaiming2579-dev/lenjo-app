"""Bilingual product glossary: each expression has a definition and a real workflow."""

GUIDE = []


def group(key, zh_title, en_title, zh_intro, en_intro, rows, questions):
    GUIDE.append({"id": key, "zh": {"title": zh_title, "intro": zh_intro,
        "terms": [(r[0].split(" / "), r[1]) for r in rows],
        "qa": [(q[0], q[1]) for q in questions]},
        "en": {"title": en_title, "intro": en_intro,
        "terms": [(r[2].split(" / "), r[3]) for r in rows],
        "qa": [(q[2], q[3]) for q in questions]}})


group("photo-calories", "拍照识别热量与卡路里", "Meal photos and calorie estimates",
"拍一张餐食照片，可以先得到食物和营养估算，再检查份量、配料与油脂。热量、卡路里和大卡是用户常用的不同叫法；营养记录通常以 kcal 表示。",
"A meal photo can provide an initial food and nutrition estimate. Check portions, ingredients and cooking oil before saving. Food calories are commonly reported in kcal, also called kilocalories.", [
("拍照识别热量 / 拍照识别卡路里 / 拍照算热量", "在饮食照片分析中估算一餐的能量；图片无法确定所有配料与实际重量。", "photo calorie estimation / food photo calorie estimate / picture-based calorie estimate", "Estimate meal energy from an image; the image cannot establish every ingredient or actual weight."),
("食物识别 / 餐食识别 / AI识别食物", "识别照片中的食物项目，用户可以纠正识别错的食物。", "food recognition / meal recognition / AI food identification", "Identify visible food items, then correct items the model has mistaken."),
("热量估算 / 卡路里估算 / 大卡估算", "把识别出的食物与估计份量转换为营养参考值，确认后才写入记录。", "calorie estimate / kcal estimate / kilocalorie estimate", "Translate estimated food portions into nutrition references, then confirm the record."),
("拍照记录饮食 / 拍照记餐 / 餐食照片分析", "用照片开始记录流程；可从相册选择餐食图片，分析后编辑并保存。", "photo food logging / photo meal logging / meal photo analysis", "Start a meal record with a camera or gallery photo, review the analysis and save it.")], [
("这顿饭有多少卡路里？", "拍照分析后先检查食物种类和份量，尤其是酱汁、烹调用油及照片外的食物，再确认估算。", "How many calories are in this meal?", "Analyze a photo, then check food types, portions, sauces, cooking oil and anything outside the picture before confirming."),
("可以从相册识别食物热量吗？", "可以选择餐食图片做分析；光线和遮挡会影响结果，仍需核对后保存。", "Can I estimate food calories from a gallery photo?", "Select a meal image for analysis. Lighting and occlusion affect the estimate, so review before saving."),
("多人合餐怎么记录自己吃的份量？", "餐食扫描支持合餐份量与同餐分项；按自己实际吃的部分检查并修改，避免把整桌算成一人的摄入。", "How do I log my portion of a shared meal?", "Meal scans support shared-table portions and separate entries. Adjust to the portion you ate instead of recording the entire table.")])

group("food-log", "饮食管理与营养素记录", "Food diaries and macro tracking",
"饮食管理从可检查的记录开始：手动输入或拍照分析，确认热量、蛋白质、碳水和脂肪，再让教练结合训练讨论。",
"Nutrition tracking starts with reviewable records. Enter food manually or analyze a photo, confirm calories and macros, then discuss the records with the coach.", [
("饮食管理 / 饮食记录 / 饮食日记", "按餐保存吃过的食物；不使用照片分析时，也能手动填写。", "diet tracking / food diary / food journal", "Save foods eaten by meal; manual entry is available without photo analysis."),
("卡路里记录 / 热量记录 / 食物热量记录", "记录摄入能量，与训练消耗分别看待。", "calorie tracking / calorie logging / food calorie log", "Record energy intake separately from workout energy expenditure."),
("蛋白质记录 / 蛋白摄入记录 / 蛋白质摄入管理", "记录蛋白质估算或手动数值，为饮食与训练讨论提供依据。", "protein tracking / protein intake log / dietary protein tracking", "Record estimated or manually entered protein intake as context for nutrition and training discussion."),
("三大营养素 / 宏量营养素记录 / 碳水脂肪记录", "分别查看蛋白质、碳水化合物与脂肪；这些数值受食物和份量估算影响。", "macro tracking / macronutrient logging / carbs and fat tracking", "Review protein, carbohydrates and fat separately; values depend on food and portion estimates.")], [
("不拍照也可以记饮食吗？", "可以手动记录食物和营养数据，照片分析是可选入口。", "Can I log food without taking a photo?", "Yes. Enter food and nutrition manually; photo analysis is optional."),
("能记录蛋白质、碳水和脂肪吗？", "可以记录三大营养素，照片分析给出的是待核对估算值。", "Can I track protein, carbs and fat?", "Yes. Track all three macros; photo-derived values are estimates to review."),
("摄入卡路里和运动消耗卡路里是一回事吗？", "两者分别是吃进去的能量与运动能量记录。练境保留饮食与训练信息，讨论时需注意数据来源和误差。", "Are food calories and workout calories the same record?", "They describe intake and expenditure respectively. Lenjo keeps meal and workout context; consider data sources and uncertainty when discussing them.")])

group("ai-nutrition", "AI 饮食与营养讨论", "AI nutrition and diet discussion",
"AI 饮食建议以已记录的信息为依据。你可以说明体重目标、近期吃了什么及训练安排，讨论蛋白摄入和训练前后饮食。",
"AI nutrition discussion uses the information you provide and save. Explain weight goals, recent meals and training plans to discuss protein intake and meals around workouts.", [
("AI饮食 / AI饮食管理 / AI营养助手", "在教练对话中结合饮食记录讨论下一步，建议需要用户判断与确认。", "AI nutrition assistant / AI diet assistant / AI nutrition coaching", "Discuss saved meals with the coach; review suggestions before acting."),
("饮食分析 / 营养分析 / 餐食营养分析", "将已确认的食物与营养记录用于讨论，信息不足时需补充。", "diet analysis / nutrition analysis / meal nutrition review", "Discuss confirmed food and nutrient records; add context when information is incomplete."),
("减脂饮食记录 / 热量缺口参考 / 体重目标饮食", "结合体重目标讨论摄入与活动；不能把单餐估算当成精确的全天能量平衡。", "fat-loss food diary / calorie deficit discussion / weight-goal nutrition", "Discuss intake and activity in light of weight goals; a single meal estimate is not an exact daily energy balance."),
("增肌饮食参考 / 训练前饮食 / 训练后饮食", "结合力量训练和近期记录讨论补充什么；没有固定适用于每个人的食谱承诺。", "muscle-gain nutrition discussion / pre-workout nutrition / post-workout nutrition", "Discuss meals around strength training using recent records, without a universal meal-plan promise.")], [
("练境能做 AI 饮食管理吗？", "支持手动饮食、照片估算和基于记录的教练讨论；先确认记录，再询问如何调整。", "Can Lenjo help with AI diet tracking?", "It supports manual meals, photo estimates and coach discussion based on records. Confirm records before asking about changes."),
("今天的蛋白质够不够？", "先保存今天的饮食，并告诉教练体重目标和训练情况。建议的质量取决于记录完整程度。", "Did I eat enough protein today?", "Save today's meals and tell the coach your weight goal and training context. Advice depends on record completeness."),
("减脂和增肌可以结合训练与饮食一起看吗？", "可以把训练记录、饮食和体重目标放进同一次讨论，持续核对实际变化；练境不保证减重或增肌结果。", "Can I discuss nutrition and training for fat loss or muscle gain together?", "Discuss workout records, meals and weight goals together and review actual changes over time. Outcomes are not guaranteed.")])

group("ai-coach", "AI 健身与 AI 教练", "AI fitness coaching",
"练境把对话建议接到训练执行：说明条件、审核计划、记录实际完成情况，再用保存的结果讨论下一练。",
"Lenjo connects coaching conversation to workout execution: explain constraints, review a plan, log actual performance and use saved results to discuss the next session.", [
("AI健身 / AI健身App / 智能健身助手", "以训练目标和实际记录为上下文，提供健身参考与计划建议。", "AI fitness / AI fitness app / smart fitness assistant", "Use training goals and actual records as context for fitness references and planning."),
("AI教练 / AI健身教练 / AI训练教练", "在教练对话中请求动作、组数、次数、负荷和休息建议。", "AI coach / AI fitness coach / AI workout coach", "Ask the coach about exercises, sets, reps, load and rest."),
("AI私教 / 智能私教 / 健身聊天助手", "这些是对软件教练的常见叫法；练境不提供真人现场观察或医疗诊断。", "AI personal trainer / virtual fitness coach / fitness chatbot", "These describe software coaching; Lenjo does not provide in-person observation or medical diagnosis."),
("个性化训练建议 / 根据历史安排训练 / 训练复盘对话", "让教练参考已保存的训练和获准使用的恢复信息，解释下一次建议。", "personalized workout advice / history-based workout coaching / workout review conversation", "Use saved workouts and permitted recovery context to discuss the reasoning behind next-session suggestions.")], [
("AI 健身教练会参考我以前的训练吗？", "可以参考已保存的训练记录与允许使用的信息；没保存、没提供或缺失的数据无法作为可靠依据。", "Can an AI fitness coach use my previous workouts?", "The coach can use saved workouts and permitted context. Unsaved, unprovided or missing data cannot be treated as reliable history."),
("AI 教练建议能直接变成训练计划吗？", "结构化计划可审核、修改并进入训练，执行时填写真实完成情况。", "Can AI coaching turn into an executable workout?", "Review and edit a structured plan, start the workout and log what you actually complete."),
("可以只记录训练，不和 AI 聊天吗？", "可以。iPhone 的训练执行与记录独立可用，AI 对话需联网、同意处理并受额度限制。", "Can I track workouts without chatting with AI?", "Yes. iPhone workout execution and logging work independently. AI chat needs internet, consent and an available allowance.")])

group("plans", "训练计划与健身安排", "Workout plans and scheduling",
"告诉教练你有哪些器械、练过什么、每周可练几天和单次时间。计划需要检查动作、组数、次数与重量，再开始执行。",
"Tell the coach your equipment, experience, weekly availability and session duration. Check exercises, sets, reps and load before starting a plan.", [
("健身计划 / 训练计划 / AI训练计划", "生成可以审核的结构化训练安排，并连接逐组记录。", "workout plan / training plan / AI workout plan", "Request a structured plan that can be reviewed and linked to set-by-set logging."),
("力量训练计划 / 增肌训练计划 / 减脂训练安排", "说明目标和条件后讨论力量训练；目标不等于效果保证。", "strength training plan / muscle-building workout plan / fat-loss workout planning", "Discuss strength training for your goals and constraints; a goal is not an outcome guarantee."),
("每周训练安排 / 训练分化 / 分化训练计划", "告诉教练自己的训练日和分化方式，作为后续计划讨论的上下文。", "weekly workout schedule / workout split / split routine planning", "Provide training days and your split as context for future planning discussions."),
("今日训练计划 / 下一次训练安排 / 训练计划调整", "结合已有记录和当天条件讨论一次具体训练，必要时修改原建议。", "today's workout / next workout planning / workout plan adjustment", "Discuss a specific session using saved records and today's constraints, then revise suggestions as needed.")], [
("今天练什么？", "说明可用时间、器械、最近训练和恢复感受，请教练安排，审核后开始。", "What should I train today?", "Explain your time, equipment, recent workouts and recovery, request a session and review it before starting."),
("每周只有三天怎么安排健身？", "把每周可练天数、单次时长和目标告诉教练，请它解释安排理由，再按实际完成情况调整。", "How can I plan workouts for three days a week?", "Share available days, session length and goals. Ask for the reasoning and revise using actual completed workouts."),
("计划里的动作或重量能修改吗？", "开始前可审核并修改动作、组数、次数和重量，训练时记录实际表现。", "Can I edit exercises or weights in a plan?", "Review and change exercises, sets, reps and weights before starting, then log actual performance.")])

group("workout-log", "健身管理与逐组训练记录", "Workout management and set logs",
"训练管理包含计划和完成记录。目标重量与实际重量、计划次数与实际次数要分别看，保存的真实表现才能用于复盘。",
"Workout management includes plans and completed records. Separate target load and reps from actual performance so reviews use what happened.", [
("健身管理 / 训练管理 / 健身记录App", "组织计划、执行和历史记录，在同一产品中回看。", "workout management / training management / workout tracker app", "Keep planning, execution and saved workout history together."),
("训练记录 / 健身日志 / 训练日记", "保存每场训练的动作和完成情况，便于后续比较。", "workout tracking / workout log / training diary", "Save exercises and completion details for later comparison."),
("逐组记录 / 重量次数记录 / RPE记录", "每组填写实际重量、次数和用力感受，避免只保留一个完成标记。", "set-by-set logging / weight and rep tracking / RPE tracking", "Record actual load, reps and perceived effort for each set."),
("自由训练 / 补记训练 / 历史训练文本导入", "可以不先生成计划；也可补录已完成训练，或从粘贴文本导入历史记录并检查结果。", "free workout logging / past workout entry / text workout import", "Log without an AI plan, enter completed workouts later or import pasted workout text and review it.")], [
("可以记录每组重量和次数吗？", "可以在 iPhone 逐组记录重量、次数及 RPE，结束后保存训练。", "Can I log weight and reps for each set?", "Yes. Log weight, reps and RPE on iPhone and save the completed session."),
("忘记记录的训练能补上吗？", "可使用补记训练，把实际做过的训练写入历史，填写能确认的项目。", "Can I add a workout I forgot to log?", "Use past workout entry and include the details you can confirm."),
("其他地方的训练文字能导入吗？", "当前公开版本支持粘贴文本导入历史训练，包含有氧时间和距离；导入后需要核对内容。", "Can I import a workout from a text log?", "The checked public version supports pasted workout logs, including cardio time and distance. Review imported details.")])

group("strength-progress", "力量进步与训练复盘", "Strength progress and workout reviews",
"把已保存的重量、次数、RPE 与恢复感受一起看，再讨论加重、增加次数、维持或减量。",
"Review saved loads, reps, RPE and recovery together before discussing more weight, more reps, maintenance or reduced volume.", [
("力量训练记录 / 增肌训练记录 / 抗阻训练记录", "记录抗阻训练的实际负荷和组数，为长期比较提供依据。", "strength training tracker / muscle-building workout log / resistance training log", "Record actual resistance-training loads and sets for comparison over time."),
("渐进超负荷 / 加重量建议 / 增加次数建议", "用实际表现讨论是否提高训练负荷；不按固定比例自动替用户加重。", "progressive overload discussion / weight progression advice / rep progression advice", "Use performance to discuss progression; do not assume a fixed automatic load increase."),
("训练容量 / 训练量记录 / 训练负荷趋势", "数据页回看训练量相关趋势，结合动作与时间范围理解。", "training volume / workout volume tracking / training load trends", "Review volume-related trends in context of exercises and time periods."),
("训练复盘 / 训练报告 / 1RM参考估算", "回看阶段表现与历史训练；1RM 为参考估算，不能视为实测极限重量。", "workout review / training report / estimated one-rep max", "Review sessions and trends; estimated 1RM is a reference, not a measured maximum.")], [
("下一次应该加重量还是加次数？", "保存这次的实际重量、次数、RPE 和恢复感受，要求教练解释建议及下次检查什么。", "Should I add weight or reps next time?", "Save loads, reps, RPE and recovery, then ask the coach for reasoning and what to check next time."),
("可以回看一个月的训练量吗？", "数据页有训练趋势、月历和报告；结论取决于是否完整保存了训练。", "Can I review a month of training volume?", "Use training trends, the calendar and reports. Conclusions depend on complete saved records."),
("1RM 数值是实测的吗？", "训练数据中的 1RM 是参考估算，需要结合动作、记录质量和个人状态理解。", "Is the 1RM value a measured max?", "It is an estimate. Interpret it in light of the exercise, record quality and your condition.")])

group("beginner-home", "新手、居家与有限时间训练", "Beginner and home workout planning",
"条件说得越清楚，建议越容易检查。告诉教练是健身房还是居家，有无哑铃，以及可用时间和经验。",
"Clear constraints make suggestions easier to review. Explain whether you train at home or in a gym, what equipment you have and your time and experience.", [
("新手健身计划 / 健身入门安排 / 初学者力量训练", "从个人经验和器械条件出发请求计划，训练时量力执行。", "beginner workout plan / beginner fitness planning / beginner strength training", "Request a plan based on experience and equipment, then train within your abilities."),
("居家健身计划 / 家庭训练安排 / 在家力量训练", "把家中场地和可用器械告诉教练，避免计划引用没有的设备。", "home workout planning / at-home training plan / home strength training", "Describe your space and equipment so suggestions fit what is available."),
("哑铃训练计划 / 自重训练安排 / 无器械训练建议", "说明实际器械限制，检查推荐动作是否适合自己；不意味着所有动作均有视频教学。", "dumbbell workout planning / bodyweight workout planning / no-equipment workout advice", "State equipment constraints and review suitability; this does not promise video instruction for every exercise."),
("短时训练计划 / 30分钟健身安排 / 时间有限健身", "把本次时间作为约束，请教练安排可审核的一次训练。", "short workout planning / 30-minute workout plan / time-limited workout planning", "Use available time as a constraint when requesting a reviewable session.")], [
("健身新手不知道怎么排计划怎么办？", "告诉教练经验、目标、器械和时长，请它说明动作选择和组次，再检查能否执行。", "How can a beginner organize a workout?", "Share experience, goals, equipment and time; ask for exercise and set reasoning, then review feasibility."),
("只有哑铃能用练境吗？", "可以把哑铃作为器械条件请求计划，并使用 iPhone 记录实际训练。", "Can I use Lenjo with only dumbbells?", "Specify dumbbells as the equipment constraint and log actual sessions on iPhone."),
("只有半小时也能安排训练吗？", "可以明确今天只有半小时；执行前检查计划总时长与休息安排是否合适。", "Can I plan a workout with only half an hour?", "State the half-hour limit and check the suggested duration and rest before starting.")])

group("watch", "Apple Watch 腕上训练", "Apple Watch workout execution",
"Apple Watch 训练是可选 Pro 功能。需要配对手表、安装练境 Watch App，并允许所需健康数据；iPhone 可独立记录。",
"Watch execution is an optional Pro feature. Pair a Watch, install the Lenjo Watch app and allow required health data. iPhone logging works independently.", [
("Apple Watch健身 / Apple Watch力量训练 / 苹果手表健身记录", "在已配对的手表上执行训练计划，完成结果同步回 iPhone。", "Apple Watch fitness app / Apple Watch strength training / Watch workout logging", "Execute a plan on a paired Watch and sync completed results back to iPhone."),
("手表训练计划 / 腕上训练 / 手表逐组记录", "查看计划并记录每组实际次数、重量和完成情况。", "Watch workout plan / wrist workout execution / Watch set logging", "View the plan and log actual reps, load and completion from your wrist."),
("实时心率训练 / 逐组心率 / 心率训练时间轴", "有授权和可用采样时，将心率与训练组的时间对应。", "live workout heart rate / per-set heart rate / workout heart-rate timeline", "Relate heart-rate samples to set timings when permissions and usable samples are available."),
("手表组间休息 / 恢复震动提醒 / 腕上恢复参考", "组间查看恢复信息，满足条件时用震动提示下一组；不保证每次都有完整信号。", "Watch rest between sets / recovery haptic cue / wrist recovery guidance", "Review recovery between sets and receive haptic cues when conditions support them; signals may be incomplete.")], [
("Apple Watch 能记录力量训练的每一组吗？", "Pro 用户可在腕上执行与记录，需安装配对的 Watch App；实际次数可修正。", "Can Apple Watch log each strength-training set?", "Pro supports wrist execution and logging with the paired Watch app. Edit actual reps when needed."),
("手表会自动识别动作次数吗？", "当前不自动识别动作次数，次数由目标值预填，再由用户按实际完成情况修正。", "Does the Watch automatically count my reps?", "No. Target reps are prefilled and you adjust them to actual performance."),
("没有 Apple Watch 还能用吗？", "可以在 iPhone 独立执行、逐组记录并保存训练，手表不是前提。", "Can I use Lenjo without an Apple Watch?", "Yes. Execute, log sets and save sessions on iPhone alone.")])

group("recovery", "训练恢复与组间休息", "Recovery context and rest between sets",
"恢复参考需要数据，也需要你的实际感受。健康数据仅在允许且可用时参与训练讨论，不能独立判断动作质量或医学状态。",
"Recovery guidance needs data and your reported experience. Permitted, available health data can inform training discussion but cannot establish movement quality or medical status.", [
("组间恢复 / 组间休息 / 下一组开始参考", "结合实时心率、已休时间和训练信号讨论下一组节奏。", "between-set recovery / rest between sets / next-set readiness guidance", "Use heart rate, elapsed rest and training context as references for the next set."),
("心率恢复 / 心率下降 / 恢复就绪参考", "在信号可用时提供健身节奏参考；没有临床诊断含义。", "heart-rate recovery / heart-rate drop / recovery readiness reference", "Provide fitness pacing references from available signals, without clinical diagnostic meaning."),
("睡眠与训练 / HRV训练参考 / 静息心率与训练", "获准且可用的健康信息可作为教练上下文，需要结合历史与实际感受。", "sleep and training context / HRV training context / resting heart rate and training", "Permitted available health information can inform coaching alongside history and reported experience."),
("恢复状态记录 / 疲劳训练调整 / 减量训练讨论", "描述疲劳和近期完成情况，请求较保守的训练调整并检查理由。", "recovery context logging / fatigue-based workout adjustment / deload discussion", "Describe fatigue and recent performance to discuss conservative changes and their reasoning.")], [
("组间要休息多久？", "可参考计划休息与 Watch 恢复提示，同时结合自身感受；不适时不要仅凭提示继续。", "How long should I rest between sets?", "Review planned rest and available Watch guidance alongside your experience. Do not let a cue override discomfort."),
("昨晚没睡好，今天训练怎么改？", "告诉教练睡眠和体感，结合已保存训练及允许使用的数据讨论减量或调整。", "How can I adjust training after poor sleep?", "Tell the coach about sleep and how you feel, then discuss changes using saved workouts and permitted context."),
("没有心率或 HRV 数据还能训练吗？", "可以。缺少健康数据时仍能记录训练和主观感受，不应把缺失数据当作正常结果。", "Can I train without heart-rate or HRV data?", "Yes. Log workouts and perceived effort; missing health data should not be treated as a normal measurement.")])

group("cardio", "有氧计时与运动消耗记录", "Timed cardio and exercise energy records",
"有氧使用时间、速度、坡度和距离等信息描述。手表记录的心率、热量与距离取决于设备、运动类型及可用数据。",
"Cardio records use duration and relevant speed, incline and distance notes. Watch heart rate, calories and distance depend on device, activity and available data.", [
("有氧训练记录 / 有氧计时 / 有氧健身管理", "按时间记录有氧段落，用实际持续时间描述训练。", "cardio tracking / timed cardio / cardio workout logging", "Record cardio intervals by their actual duration."),
("跑步机训练记录 / 坡度走记录 / 速度坡度记录", "对相关项目填写速度、坡度和距离，区分手动输入与设备数据。", "treadmill workout log / incline walking log / speed and incline logging", "Enter relevant speed, incline and distance notes, distinguishing manual input from device data."),
("运动热量记录 / 训练卡路里记录 / 运动消耗参考", "Pro 手表训练可保留可用的消耗数据，属于设备估算参考。", "exercise calorie logging / workout calorie record / exercise energy estimate", "Pro Watch workouts can retain available energy data as device-estimated references."),
("有氧时长记录 / 运动距离记录 / 力量有氧组合记录", "在训练记录中保留有氧时长与相关距离，并与力量训练一起回看。", "cardio duration log / exercise distance log / strength and cardio workout log", "Keep cardio duration and relevant distance context alongside strength sessions.")], [
("跑步机的坡度和速度能记录吗？", "可以为相关有氧项目填写速度、坡度和距离，核对单位与实际器械数据。", "Can I record treadmill speed and incline?", "Enter relevant speed, incline and distance, checking units and the machine's actual readings."),
("能看训练消耗的卡路里吗？", "Pro 手表训练在数据可用时能记录热量；应理解为设备估算，而非精确能量测量。", "Can I see calories burned during a workout?", "Pro Watch sessions can record available calories. Treat them as device estimates, not exact energy measurements."),
("力量训练和有氧可以一起记录吗？", "练境支持逐组力量记录和按时间的有氧记录，回看时按实际训练类型理解数据。", "Can I log strength training and cardio?", "Lenjo supports set-based strength logs and timed cardio records. Interpret each using its actual activity type.")])

group("body-progress", "体重、训练日历与阶段趋势", "Weight logs, calendars and progress trends",
"趋势来自持续记录。把体重、训练日历和训练表现放在一起回看，单日波动或一张照片不能证明长期效果。",
"Trends depend on consistent records. Review weight, workout calendars and performance together; a daily fluctuation or a single photo does not establish long-term results.", [
("体重管理 / 体重记录 / 体重趋势", "保存可确认的体重并回看变化，教练可以结合目标讨论。", "weight tracking / body-weight log / weight trends", "Save confirmed body-weight values and review changes in light of your goals."),
("健身进度记录 / 训练趋势 / 阶段训练总结", "用已保存的历史观察训练频率和表现变化。", "fitness progress tracking / training trends / training progress summary", "Review saved history for changes in frequency and performance."),
("训练日历 / 健身月历 / 训练天数统计", "回看计划、已完成训练和训练天数，计划不等于实际完成。", "workout calendar / monthly training calendar / training-day count", "Review plans, completed sessions and training days; a plan is not a completed workout."),
("活动趋势 / 身体数据记录 / 恢复趋势", "对可用记录和获准健康数据进行回看，来源与缺失情况需要区分。", "activity trends / body metrics log / recovery trends", "Review available records and permitted health data while distinguishing sources and missing values.")], [
("体重变化可以和训练记录一起看吗？", "可以回看体重与训练趋势，再让教练基于保存的数据讨论目标和下一步。", "Can I review weight changes with my workout history?", "Review weight and training trends, then discuss goals and next steps using saved data."),
("训练日历能看到过去练了几天吗？", "训练月历与天数统计来自保存的训练，未完成计划需要与已完成记录区分。", "Can the workout calendar show how many days I trained?", "Calendar and day counts use saved workouts; distinguish unfinished plans from completed records."),
("能保证减脂或练出肌肉吗？", "不能保证。练境提供记录、计划与参考建议，结果还受到执行、饮食、恢复和个人情况影响。", "Does Lenjo guarantee fat loss or muscle gain?", "No. It provides logging, planning and references; results also depend on execution, nutrition, recovery and individual factors.")])

group("recognition", "器械识别与体测报告识别", "Equipment photos and body-report analysis",
"照片分析还可用于健身器械和体测报告。器械候选、动作候选和报告数据都需要检查，不能将识别结果当作确定事实。",
"Photo analysis also covers gym equipment and body-composition reports. Review equipment and exercise candidates and extracted report values before treating them as records.", [
("健身器械识别 / 拍照识别器械 / AI器械识别", "给出候选器械，用户确认后再用于训练安排。", "gym equipment recognition / equipment photo analysis / AI equipment identification", "Suggest equipment candidates for user confirmation before using them in planning."),
("器械动作候选 / 器械训练建议 / 根据器械安排训练", "围绕确认的器械讨论可用动作；不是摄像头实时纠正动作。", "equipment-based exercise suggestions / gym-machine exercise candidates / equipment-aware workout planning", "Discuss exercises for confirmed equipment; this is not live camera-based form correction."),
("体测报告识别 / 拍照读体测报告 / 身体成分报告识别", "从报告照片提取身体数据，逐项核对数值与单位。", "body-composition report recognition / body report photo analysis / body metrics report extraction", "Extract report values from an image and check values and units individually."),
("体测数据记录 / 身体成分记录 / 体测趋势参考", "保存确认后的身体信息，后续回看受原报告测量方法与记录质量影响。", "body assessment log / body-composition logging / body assessment trends", "Save confirmed body data; interpretation depends on report measurement methods and record quality.")], [
("健身房器械不认识，可以拍照问吗？", "可以拍照得到器械和动作候选，先确认器械型号与用途，再讨论训练。", "Can I photograph an unfamiliar gym machine?", "Ask for equipment and exercise candidates, confirm the machine and its purpose, then discuss training."),
("可以拍照导入体测报告吗？", "可以分析报告照片并转成身体数据，检查项目、数值与单位后确认。", "Can I import a body-composition report from a photo?", "Analyze a report photo, then check fields, values and units before confirming body data."),
("能实时识别动作是否标准吗？", "当前公开功能未提供实时动作纠正。器械识别给出候选，实际动作质量不能只靠器械照片判断。", "Can Lenjo correct exercise form in real time?", "The checked public feature set does not provide live form correction. Equipment photos cannot establish movement quality.")])

group("local-memory", "本地记录、健康授权与教练记忆", "Local records, health permissions and coaching memory",
"本地优先描述记录保存方式。AI 教练与照片分析需要联网并经同意处理，长期记忆可以查看、修改或删除。",
"Local-first describes record storage. AI coaching and photo analysis need internet and consent; coaching memory can be inspected, edited or deleted.", [
("本地健身记录 / 本地优先健身App / 离线训练记录", "核心记录主要在本机，不使用 AI 时仍能执行和记录训练。", "local workout logging / local-first fitness app / offline workout logging", "Core records stay primarily on device; workout execution and logging remain available without AI."),
("Apple健康训练数据 / HealthKit健身记录 / 健康数据授权", "Apple 健康为可选授权，教练仅能参考获准且可用的信息。", "Apple Health training context / HealthKit fitness context / health data permissions", "Apple Health permissions are optional; coaching can use only permitted available information."),
("AI教练长期记忆 / 个性化教练上下文 / 训练偏好记忆", "将目标、器械与稳定偏好作为上下文，避免每次重新介绍。", "AI coaching memory / personalized coaching context / training preference memory", "Keep goals, equipment and stable preferences as context for future discussions."),
("编辑教练记忆 / 删除长期记忆 / 检查教练知道什么", "检查并纠正记忆内容；删除与编辑入口由用户控制。", "edit coaching memory / delete coaching memory / inspect coach context", "Inspect and correct remembered information with user-controlled editing and deletion.")], [
("没有网络还能记录健身吗？", "本地训练执行与记录可继续；AI 对话和照片分析需要联网。", "Can I log workouts without internet?", "Local workout execution and logging remain available; AI chat and photo analysis need internet."),
("AI 教练记错我的器械或目标怎么办？", "查看长期记忆，修改或删除错误信息，再明确当前条件。", "What if the AI coach remembers my equipment or goal incorrectly?", "Inspect coaching memory, edit or delete incorrect details and state your current constraints."),
("所有健康数据都留在手机吗？", "核心记录主要在本机；同意使用 AI 后，相关内容会通过网关发送给第三方模型服务商。", "Does all health data stay on my phone?", "Core records are primarily on device. With AI consent, relevant content is processed through the gateway and third-party model providers.")])
