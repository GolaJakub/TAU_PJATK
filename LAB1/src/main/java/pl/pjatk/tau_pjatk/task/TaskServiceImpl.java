package pl.pjatk.tau_pjatk.task;

import java.util.ArrayList;
import java.util.List;
import org.springframework.stereotype.Service;

@Service
public class TaskServiceImpl implements TaskService {
    private List<Task> tasks = new ArrayList<>();
    private Long nextId = 1L;

    @Override
    public List<Task> getAllTasks() {
        return tasks;
    }

    @Override
    public Task getTaskById(Long id) {
        for (Task task : tasks) {
            if (task.getId().equals(id)) {
                return task;
            }
        }
        return null;
    }

    @Override
    public Task createTask(Task task) {
        task.setId(nextId);
        nextId++;
        tasks.add(task);
        return task;
    }

    @Override
    public Task updateTask(Long id, Task task) {
        for (int i = 0; i < tasks.size(); i++) {
            if (tasks.get(i).getId().equals(id)) {
                task.setId(id);
                tasks.set(i, task);
                return task;
            }
        }
        return null;
    }

    @Override
    public void deleteTask(Long id) {
        tasks.removeIf(task -> task.getId().equals(id));
    }
}

