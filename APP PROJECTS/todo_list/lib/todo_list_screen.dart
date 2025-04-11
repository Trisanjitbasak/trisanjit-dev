import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import 'todo_list_model.dart';

class TodoListScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final todoListModel = Provider.of<TodoListModel>(context);

    return Scaffold(
      appBar: AppBar(
        title: Text('To-Do List'),
      ),
      body: ListView.builder(
        itemCount: todoListModel.todoItems.length,
        itemBuilder: (context, index) {
          final item = todoListModel.todoItems[index];
          return ListTile(
            title: Text(item.title),
            trailing: Checkbox(
              value: item.isDone,
              onChanged: (bool? value) {
                item.isDone = value ?? false;
                todoListModel.updateTodoItem(index, item);
              },
            ),
            onLongPress: () {
              todoListModel.deleteTodoItem(index);
            },
          );
        },
      ),
      floatingActionButton: FloatingActionButton(
        child: Icon(Icons.add),
        onPressed: () {
          showDialog(
            context: context,
            builder: (context) {
              return AlertDialog(
                title: Text('Add To-Do Item'),
                content: TextField(
                  onSubmitted: (value) {
                    final newItem = TodoItem(title: value);
                    todoListModel.addTodoItem(newItem);
                    Navigator.of(context).pop();
                  },
                ),
              );
            },
          );
        },
      ),
    );
  }
}
