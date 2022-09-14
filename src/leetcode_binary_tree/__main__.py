"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Leetcode Binary Tree."""


if __name__ == "__main__":
    main(prog_name="leetcode-binary-tree")  # pragma: no cover
