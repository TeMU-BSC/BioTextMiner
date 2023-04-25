import { Card, CardContent, Typography } from '@mui/material';


const ExampleCard = () => {
  return (
    <div className="w-96 mx-auto">
      <Card className="bg-white shadow-md rounded-lg overflow-hidden">
        <CardContent>
          <Typography variant="h5" component="h2" className="font-bold mb-4">
            Card Title
          </Typography>
          <Typography variant="body2" component="p" className="text-gray-700 mb-4">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam ut leo ac turpis malesuada semper. Praesent aliquet est vitae augue tristique euismod. Curabitur rutrum tincidunt nulla, non bibendum erat tempus a. Donec vel magna nec augue interdum maximus. Duis facilisis felis eget tortor ullamcorper tincidunt. Nullam fringilla est et purus tristique, vel aliquet metus scelerisque. Sed non lacus ut ex faucibus bibendum. Proin sed nibh eget est eleifend lobortis. 
          </Typography>
          <button type="button" className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">
            Action
          </button>
        </CardContent>
      </Card>
    </div>
  );
};

export default ExampleCard;
