package pl.pjatk.tau_pjatk.task;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.Mockito;
import org.mockito.MockitoAnnotations;

import java.util.Arrays;
import java.util.List;

public class TaskControllerTest {

    /*Użyte asercje: assertEquals, assertFalse, assertTrue, assertNull, assertNotNull*/

    @InjectMocks
    private TaskController taskController;

    @Mock
    private TaskService taskService;

    @BeforeEach
    public void setup() {
        MockitoAnnotations.openMocks(this);
    }

    @Test
    public void testGetAllTasks() {
        // Given
        Task task1 = new Task(1L, "Task 1", false);
        Task task2 = new Task(2L, "Task 2", true);
        Mockito.when(taskService.getAllTasks()).thenReturn(Arrays.asList(task1, task2));

        // When
        List<Task> tasks = taskController.getAllTasks();

        // Then
        assertEquals(2, tasks.size());
        assertEquals("Task 1", tasks.get(0).getName());
        assertFalse(tasks.get(0).isCompleted());
        assertEquals("Task 2", tasks.get(1).getName());
        assertTrue(tasks.get(1).isCompleted());
    }

    @Test
    public void testGetTaskById() {
        // Given
        Task task = new Task(1L, "Task 1", false);
        Mockito.when(taskService.getTaskById(1L)).thenReturn(task);

        // When
        Task result = taskController.getTaskById(1L);

        // Then
        assertEquals("Task 1", result.getName());
        assertFalse(result.isCompleted());
    }

    @Test
    public void testCreateTask() {
        // Given
        Task taskToCreate = new Task(null, "New Task", true);
        Task createdTask = new Task(1L, "New Task", true);
        Mockito.when(taskService.createTask(taskToCreate)).thenReturn(createdTask);

        // When
        Task result = taskController.createTask(taskToCreate);

        // Then
        assertNotNull(result.getId());
        assertEquals("New Task", result.getName());
        assertTrue(result.isCompleted());
    }

    @Test
    public void testUpdateTask() {
        // Given
        Task updatedTask = new Task(1L, "Updated Task", true);
        Mockito.when(taskService.updateTask(1L, updatedTask)).thenReturn(updatedTask);

        // When
        Task result = taskController.updateTask(1L, updatedTask);

        // Then
        assertEquals(1L, result.getId());
        assertEquals("Updated Task", result.getName());
        assertTrue(result.isCompleted());
    }

    @Test
    public void testDeleteTask() {
        // When
        taskController.deleteTask(1L);

        // Then
        Mockito.verify(taskService).deleteTask(1L);
    }

    @Test
    public void testGetAllTasksWhenEmpty() {
        // Given
        Mockito.when(taskService.getAllTasks()).thenReturn(Arrays.asList());

        // When
        List<Task> tasks = taskController.getAllTasks();

        // Then
        assertTrue(tasks.isEmpty());
    }

    @Test
    public void testGetTaskByIdNotFound() {
        // Given
        Mockito.when(taskService.getTaskById(1L)).thenReturn(null);

        // When
        Task result = taskController.getTaskById(1L);

        // Then
        assertNull(result);
    }

    @Test
    public void testUpdateTaskNotFound() {
        // Given
        Task updatedTask = new Task(1L, "Updated Task", true);
        Mockito.when(taskService.updateTask(1L, updatedTask)).thenReturn(null);

        // When
        Task result = taskController.updateTask(1L, updatedTask);

        // Then
        assertNull(result);
    }

    @Test
    public void testCreateTaskWithInvalidData() {
        // Given
        Task taskToCreate = new Task(null, null, true); // Task with no name
        Mockito.when(taskService.createTask(taskToCreate)).thenReturn(null);

        // When
        Task result = taskController.createTask(taskToCreate);

        // Then
        assertNull(result);
    }

    @Test
    public void testUpdateTaskOnNonExistingTask() {
        // Given
        Task updatedTask = new Task(3L, "Updated Task", true); // Task with ID 3 doesn't exist
        Mockito.when(taskService.updateTask(3L, updatedTask)).thenReturn(null);

        // When
        Task result = taskController.updateTask(3L, updatedTask);

        // Then
        assertNull(result);
    }
}
