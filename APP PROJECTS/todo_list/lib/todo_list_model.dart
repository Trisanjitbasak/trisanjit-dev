import 'package:flutter/foundation.dart';
import 'package:hive/hive.dart';

part 'todo_item.g.dart';

@HiveType(typeId: 0)
class TodoItem {
  @HiveField(0)
  String title;

  @HiveField(1)
  bool isDone;

  TodoItem({required this.title, this.isDone = false});
}

class TodoListModel extends ChangeNotifier {
  final Box<TodoItem> _todoBox = Hive.box<TodoItem>('todoItems');

  List<TodoItem> get todoItems => _todoBox.values.toList();

  void addTodoItem(TodoItem item) {
    _todoBox.add(item);
    notifyListeners();
  }

  void updateTodoItem(int index, TodoItem item) {
    _todoBox.putAt(index, item);
    notifyListeners();
  }

  void deleteTodoItem(int index) {
    _todoBox.deleteAt(index);
    notifyListeners();
  }
}
