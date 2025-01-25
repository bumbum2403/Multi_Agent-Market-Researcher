from transformers import Trainer, TrainingArguments, BertTokenizer, BertForSequenceClassification

def train_model_on_blog_data(blog_data):
    """Fine-tune the BERT model using the scraped blog data."""
    tokenizer = BertTokenizer.from_pretrained('google-bert/bert-base-uncased')
    model = BertForSequenceClassification.from_pretrained('google-bert/bert-base-uncased', num_labels=2)

    # Tokenize the input blog data
    inputs = tokenizer(blog_data, return_tensors='pt', padding=True, truncation=True)
    labels = [1] * len(blog_data)  # Example labels (you can adjust this)

    # Set up training arguments
    training_args = TrainingArguments(
        output_dir='./results',
        num_train_epochs=1,
        per_device_train_batch_size=8,
        logging_dir='./logs',
    )

    # Initialize Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=inputs,
        labels=labels
    )

    # Fine-tune the model
    trainer.train()
    model.save_pretrained("./fine_tuned_model")
