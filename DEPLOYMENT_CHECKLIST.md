# Pre-Deployment Checklist

Complete this checklist before deploying to Render.

## Code Quality

- [ ] All code committed to GitHub
- [ ] No debugging code left in codebase
- [ ] `DEBUG = False` in production settings
- [ ] No hardcoded credentials in code
- [ ] All imports working correctly

## Dependencies

- [ ] `requirements.txt` is up to date: `pip freeze > requirements.txt`
- [ ] All new packages are in `requirements.txt`
- [ ] `runtime.txt` specifies Python 3.11.9
- [ ] No conflicts in dependency versions

## Configuration Files

- [ ] `Procfile` exists and contains:
  - `release: python manage.py migrate`
  - `web: gunicorn config.wsgi:application`
- [ ] `build.sh` exists and is executable
- [ ] `.env.example` created with all necessary variables
- [ ] `.gitignore` includes `.env`

## Environment Setup

- [ ] SECRET_KEY is strong and unique
- [ ] DATABASE_URL format verified
- [ ] CLOUDINARY credentials obtained
- [ ] ALLOWED_HOSTS configured for production domain
- [ ] CORS_ALLOWED_ORIGINS set correctly
- [ ] CSRF_TRUSTED_ORIGINS includes all domains

## Database

- [ ] PostgreSQL database created
- [ ] Database migrations ready to run
- [ ] Backup of current database available
- [ ] Migration files committed to Git

## Static Files & Media

- [ ] `collectstatic` command works locally
- [ ] Static files are being served correctly
- [ ] Cloudinary configured for media storage
- [ ] `STATIC_ROOT` points to correct directory
- [ ] WhiteNoise middleware is enabled

## Testing

- [ ] Homepage loads correctly
- [ ] All page routes work
- [ ] Admin panel is accessible
- [ ] API endpoints respond correctly
- [ ] Images load from Cloudinary
- [ ] No console errors in browser

## Security

- [ ] HTTPS enabled on production
- [ ] No sensitive data in source code
- [ ] Secret credentials in environment variables only
- [ ] CSRF protection configured
- [ ] Security headers set
- [ ] Admin password is strong

## Documentation

- [ ] README.md is up to date
- [ ] LOCAL_SETUP.md exists
- [ ] RENDER_DEPLOYMENT_GUIDE.md exists
- [ ] SETUP_GUIDE.md exists
- [ ] Deployment steps documented

## Render Setup

- [ ] Render account created
- [ ] GitHub connected to Render
- [ ] Web Service created
- [ ] PostgreSQL service created
- [ ] Environment variables added
- [ ] Build and start commands configured

## Post-Deployment Tests

- [ ] Homepage loads: https://your-domain/
- [ ] Admin panel works: https://your-domain/admin/
- [ ] API docs accessible: https://your-domain/api/docs/
- [ ] All content displays correctly
- [ ] Forms submit successfully
- [ ] No 502 Bad Gateway errors
- [ ] Logs show no errors
- [ ] Static files load (CSS/JS/images)

## Performance & Monitoring

- [ ] Response times are acceptable
- [ ] No N+1 query problems
- [ ] Database queries optimized
- [ ] Static files cached properly
- [ ] Monitoring/metrics enabled on Render
- [ ] Backup schedule configured

## Custom Domain (if applicable)

- [ ] Custom domain added to Render
- [ ] DNS records configured
- [ ] SSL certificate generated
- [ ] ALLOWED_HOSTS includes new domain
- [ ] CSRF_TRUSTED_ORIGINS updated
- [ ] Email redirects configured (if needed)

## Content

- [ ] All client information entered
- [ ] All project details added
- [ ] Testimonials uploaded
- [ ] Images optimized and uploaded
- [ ] Content reviewed for accuracy
- [ ] No placeholder text remaining

## Backups & Recovery

- [ ] Database backup created
- [ ] Backup restoration tested
- [ ] Disaster recovery plan documented
- [ ] Contact information for support

---

## Final Verification

Before going live:

```bash
# 1. Verify everything is committed
git status
# Should show: nothing to commit, working tree clean

# 2. Check that main branch is pushed
git log --oneline -5

# 3. Verify all environment variables are set on Render
# Check Render Dashboard → Environment section

# 4. Test the deployment
curl https://your-domain/
# Should return HTML homepage
```

---

## Sign-Off

- [ ] Checklist completed
- [ ] All tests passed
- [ ] Team approved for deployment
- [ ] Backups verified
- [ ] Ready to go live

**Deployment Date:** ******\_\_\_\_******

**Deployed By:** ******\_\_\_\_******

**Time Deployed:** ******\_\_\_\_******

---

## Rollback Procedure

If issues arise after deployment:

1. Check logs in Render Dashboard
2. Review error messages
3. Fix the issue locally
4. Commit and push to GitHub
5. Render will auto-redeploy
6. Or manually click "Deploy" in Render Dashboard

In case of critical issues:

- Roll back to previous Git commit
- Push to GitHub
- Render will redeploy with previous version

---

## Post-Deployment Tasks

After successful deployment:

- [ ] Notify team of live deployment
- [ ] Update documentation with actual domain
- [ ] Monitor logs for 24 hours
- [ ] Test all user workflows
- [ ] Verify email notifications working
- [ ] Update status page (if applicable)
- [ ] Schedule regular backups
- [ ] Set up monitoring alerts

---

**Good luck with your deployment! 🚀**
