# Node.js 버전 지정
FROM node:18-alpine

# 작업 디렉터리 설정
WORKDIR /app

# package.json 및 package-lock.json 복사
COPY package*.json ./

# 프로덕션 의존성 설치
RUN npm ci --only=production

# 애플리케이션 소스 코드 복사
COPY . .

# 빌드 명령어 실행 (필요한 경우)
# RUN npm run build

# 애플리케이션 실행 포트 노출
EXPOSE 3000

# 애플리케이션 실행 명령
CMD ["npm", "start"]
