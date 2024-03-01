import os
import glob

from pathlib import Path


def export_dot_envs(
        envs_dir: Path,
        env_module: str = 'config.settings.local'
):
    running_env = env_module.split('.')[-1]

    # .envs 디렉토리 내의 모든 .env 파일 경로 가져오기
    env_files = glob.glob(os.path.join(str(envs_dir / f'.{running_env}'), ".*"))

    # 각 .env 파일을 읽어서 환경 변수로 등록
    for env_file in env_files:
        with open(env_file, 'r') as f:
            # .env 파일 내의 환경 변수를 파싱하여 등록
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    key, value = line.split("=")
                    os.environ[key.strip()] = value.strip()

if __name__ == '__main__':
    project_home = Path(__file__).resolve(strict=True).parent.parent
    env_dir = project_home / '.envs'
    export_dot_envs(
        envs_dir=env_dir,
    )