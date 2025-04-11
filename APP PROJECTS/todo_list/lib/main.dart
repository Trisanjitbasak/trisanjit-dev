import 'package:flutter/material.dart';
import 'package:hive/hive.dart';
import 'package:hive_flutter/hive_flutter.dart';
import 'package:provider/provider.dart';

import 'todo_list_model.dart';
import 'todo_list_screen.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Hive.initFlutter();
  Hive.registerAdapter(TodoItemAdapter());
  await Hive.openBox<TodoItem>('todoItems');

  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider(
      create: (_) => TodoListModel(),
      child: MaterialApp(
        title: 'Flutter To-Do List',
        theme: ThemeData(
          primarySwatch: Colors.blue,
        ),
        home: TodoListScreen(),
      ),
    );
  }
}
