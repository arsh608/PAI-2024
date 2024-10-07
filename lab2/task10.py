def build_message(**info):
    message_parts = [f"{key.capitalize()}: {value}" for key, value in info.items()]
    return ", ".join(message_parts)

summary = build_message(name="Arsh", age=20, city="karachi", occupation="Engineer")
print(summary)
