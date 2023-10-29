package pl.pjatk.tau_pjatk.task;

import lombok.AllArgsConstructor;
import lombok.Data;

@Data
@AllArgsConstructor
public class Task {
    private Long id;
    private String name;
    private boolean completed;
}

