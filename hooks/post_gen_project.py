import os
import shutil
import subprocess
import sys

def run_git_command(command, cwd, error_message):
    try:
        subprocess.run(command, cwd=cwd, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {error_message}")
        print(f"Command output: {e.stderr}")
        sys.exit(1)

def main():
    # Get the project directory
    project_dir = os.getcwd()
    
    # Initialize git repository if it doesn't exist
    if not os.path.exists(os.path.join(project_dir, '.git')):
        run_git_command(['git', 'init'], project_dir, "Failed to initialize git repository")
    
    # Paths for the template and final .gitmodules file
    template_path = os.path.join(project_dir, '.gitmodules.template')
    final_path = os.path.join(project_dir, '.gitmodules')
    
    # Copy and rename the template file
    if os.path.exists(template_path):
        shutil.copy2(template_path, final_path)
        os.remove(template_path)
        
        # Add the .gitmodules file to git
        run_git_command(['git', 'add', '.gitmodules'], project_dir, "Failed to add .gitmodules file")
        
        # Commit the .gitmodules file
        run_git_command(['git', 'commit', '-m', 'Add .gitmodules file'], project_dir, "Failed to commit .gitmodules file")
        
        # Remove existing submodule directory if it exists
        submodule_path = os.path.join(project_dir, '{{cookiecutter.project_slug}}/glowing-giggle')
        if os.path.exists(submodule_path):
            shutil.rmtree(submodule_path)
        
        # Initialize and update the submodule
        run_git_command(['git', 'submodule', 'add', '-b', '{{cookiecutter.submodule_branch}}', 
                        'https://github.com/eduardo-paes-a3data/glowing-giggle.git', 
                        '{{cookiecutter.project_slug}}/glowing-giggle'], 
                       project_dir, "Failed to add submodule")
        
        # Change to the specified branch in the submodule
        if os.path.exists(submodule_path):
            run_git_command(['git', 'checkout', '{{cookiecutter.submodule_branch}}'], 
                          submodule_path, "Failed to checkout submodule branch")
            run_git_command(['git', 'pull', 'origin', '{{cookiecutter.submodule_branch}}'], 
                          submodule_path, "Failed to pull submodule changes")

if __name__ == '__main__':
    main() 