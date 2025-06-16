# LazyTrainer

**Train your regression models with zero drama.**  
LazyML helps you get started with machine learning model training in the simplest way possible — no unnecessary complications.

---

## Why LazyTrainer?

This project was created by **MrFayntom** with a clear goal in mind:

> "I made LazyML for beginners who want to train machine learning models but feel overwhelmed by all the complexity.  
> LazyML wraps it up into a clean, lazy workflow so you can focus on *what matters* — learning and iterating."
> By mistake I save the name "Lazyml" but it was already been created by someone so I changed into Lazy trainer

---

## What it Does

- Automatically preprocesses your data
- Handles categorical encoding and scaling
- Trains a regression model (SGD for now)
- Evaluates performance (MAE, R², Accuracy)
- Plots predictions
- Saves the model, scaler, and encoders

---

## Installation

```bash
pip install lazytrainer
```
---

# LazyML – Quick Start Guide

For full details, visit the official GitHub repository:  
: [https://github.com/mrfayntom/LazyML](https://github.com/mrfayntom/LazyML)

---

## Minimal Workflow Example

```python
from lazyml.trainer import LazyTrainer

# Initialize the trainer
trainer = LazyTrainer(
    data_path="path/to/your/data.csv",          # Path to your CSV file
    target_col="TargetColumn",                  # Column name you want to predict
    features=["Feature1", "Feature2", "Feature3"],  # List of input feature column names
    categorical_cols=["Feature3"]               # List of categorical feature names (if any)
)

# Train the model
trainer.train()

# Evaluate the model
trainer.evaluate()

# Plot prediction summary
trainer.plot_summary()

# Save model, scaler and encoders
trainer.save()
trainer.save_scaler()
trainer.save_encoders()
```
# LazyML

> **Note for Followers:**  
> This project is especially for those who follow my work and are genuinely interested in my updates. The `LazyML` package is now available on PyPI, but I’d like to share a quick personal update.

## Personal Update

I'm currently caught up preparing for a few hackathons and upcoming exams, so things are a little tight on my end.

I had originally uploaded a solution and dataset for one of my hackathon projects here on GitHub, but due to the hackathon’s rules — which prohibit public sharing of solutions and datasets — I had to make that repository **private** to stay within the guidelines.

## 🤝 Thanks for Understanding

If you like `LazyML` or have any feature suggestions, feel free to open an issue or contribute. And don’t worry, once the hackathon is over, I’ll be back in full open-source spirit 

— **Mr. Phantom**


