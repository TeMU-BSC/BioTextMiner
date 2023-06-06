/**
 * @file index.tsx
 * @description manage page for admin
 * @author Siddique Muhammad
 */

/**
 * @imports
 */
import React from 'react';
import Link from 'next/link';
import { Card, CardContent, Typography, makeStyles, Zoom } from '@material-ui/core';
import { InsertDriveFile, Description, AddBox } from '@material-ui/icons';
import Layout from '@/components/Layout';


// Use styles
const useStyles = makeStyles((theme) => ({
  card: {
    width: 300,
    padding: theme.spacing(2),
    textAlign: 'center',
    transition: 'transform 0.2s',
    '&:hover': {
      transform: 'scale(1.05)',
    },
  },
  icon: {
    fontSize: 48,
    marginBottom: theme.spacing(2),
  },
}));


/**
 * @constant ManagePage
 * @description manage page section
 * @returns html manage page
 */
const ManagePage = () => {

  // Use styles
  const classes = useStyles();

  // Return html
  return (
    <Layout>
      <div className="p-10">
        <div className="text-center">
          <Typography variant="h5" component="h1">
            Welcome to the manage panel!
          </Typography>
          <Typography variant="body1" className="p-10">
            Here you can insert corpus, documents, and upload files.
          </Typography>
        </div>
        <div style={{ display: 'flex', justifyContent: 'space-between', marginTop: 20 }}>
          <Link href="/manage/corpus/insert">
            <div className="no-underline">
              <Zoom in={true}>
                <Card className={classes.card}>
                  <CardContent>
                    <AddBox className={classes.icon} />
                    <Typography variant="h6" component="h2">
                      Insert New Corpus
                    </Typography>
                  </CardContent>
                </Card>
              </Zoom>
            </div>
          </Link>

          <Link href="/manage/documents/insert">
            <div className="no-underline">
              <Zoom in={true}>
                <Card className={classes.card}>
                  <CardContent>
                    <Description className={classes.icon} />
                    <Typography variant="h6" component="h2">
                      Insert Document
                    </Typography>
                  </CardContent>
                </Card>
              </Zoom>
            </div>
          </Link>

          <Link href="/manage/documents/upload">
            <div className="no-underline">
              <Zoom in={true}>
                <Card className={classes.card}>
                  <CardContent>
                    <InsertDriveFile className={classes.icon} />
                    <Typography variant="h6" component="h2">
                      Upload File
                    </Typography>
                  </CardContent>
                </Card>
              </Zoom>
            </div>
          </Link>
        </div>
      </div>
    </Layout>
  );
};

// Export default page
export default ManagePage;
