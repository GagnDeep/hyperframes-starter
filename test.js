const { execSync } = require('child_process');
try {
  execSync('npm run check', { stdio: 'inherit' });
} catch (e) {
  console.log("Check failed");
}
