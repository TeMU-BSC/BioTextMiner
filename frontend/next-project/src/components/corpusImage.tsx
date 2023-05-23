import Box from "@mui/material/Box";
import Card from "@mui/material/Card";
import CardActions from "@mui/material/CardActions";
import CardContent from "@mui/material/CardContent";
import Button from "@mui/material/Button";
import Typography from "@mui/material/Typography";
import Chip from "@mui/material/Chip";
import Stack from "@mui/material/Stack";
export interface Corpus {
  corpus_id: number;
  corpus_name: string;
  labels: string;
  description: string;
  version: number;
  n_docs: number;
}

const CorpusImage = (data: Corpus | any) => {
  return (
    <Card sx={{ minWidth: 275 }}>
      <CardContent>
        <Typography
          sx={{ fontSize: 20, textTransform: "uppercase" }}
          color="text.primary"
          gutterBottom
        >
          {data.data["corpus_name"]}
        </Typography>
        <Typography variant="h5" component="div"></Typography>
        <Typography sx={{ mb: 1.5 }} color="text.secondary">
          {data.data["description"]}
        </Typography>
        <Typography variant="body2">{data.data["n_docs"]}</Typography>
        <Stack direction="row" spacing={1}>
          {data.data["labels"]
            ?.split(",")
            .slice(0, 5)
            .map((d) => (
              <Chip label={d} key={d}></Chip>
            ))}
        </Stack>
      </CardContent>
    </Card>
  );
};

export default CorpusImage;